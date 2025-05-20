import os 
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

# Variables esenciales
os.environ["HADOOP_HOME"] = "C:/winutils"

print("HADOOP_HOME =", os.environ.get("HADOOP_HOME"))
print("Existe winutils:", os.path.exists("C:/winutils/bin/winutils.exe"))

spark = SparkSession.builder \
    .appName("TrainALSModel") \
    .config("spark.sql.warehouse.dir", "file:///C:/tmp") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .config("spark.hadoop.home.dir", "C:/winutils") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .getOrCreate()

# Ruta de datos
base_path = Path(__file__).resolve().parent / "data"
parquet_path = str(base_path / "user_artists.parquet")

# Carga los datos
df = spark.read.parquet(parquet_path)
df = df.selectExpr("int(userID) as userID", "int(artistID) as artistID", "int(weight) as weight")

# Divide en entrenamiento y prueba
(training, test) = df.randomSplit([0.8, 0.2])

# Entrena el modelo ALS en memoria
als = ALS(
    maxIter=10,
    regParam=0.1,
    userCol="userID",
    itemCol="artistID",
    ratingCol="weight",
    coldStartStrategy="drop",
    nonnegative=True
)

model = als.fit(training)

# Evalúa
predictions = model.transform(test)
evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="weight",
    predictionCol="prediction"
)
rmse = evaluator.evaluate(predictions)
print(f"RMSE del modelo (en memoria): {rmse:.4f}")

# No se guarda el modelo por problemas con NativeIO en Windows
print("No se intentará guardar el modelo debido a incompatibilidad con Spark en Windows.")
