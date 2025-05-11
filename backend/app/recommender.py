import os
from pyspark.ml.recommendation import ALSModel, ALS
from pyspark.sql.functions import col
from app.spark_session import get_spark_session

MODEL_PATH = "./app/model/als_model"
PARQUET_PATH = "./app/parquet/user_artists.parquet"

# Cargar Spark y DataFrame UNA SOLA VEZ
spark = get_spark_session()
df = spark.read.parquet(PARQUET_PATH)
df = df.repartition(10)  # Ajusta según la capacidad de tu máquina

def load_or_train_model():
    if not os.path.exists(MODEL_PATH):
        print("Modelo no encontrado. Entrenando nuevo modelo...")
        train_and_save_model()
        return True  # Indicamos que el modelo fue entrenado
    return False  # Indicamos que el modelo ya existía


def train_and_save_model():
    als = ALS(
    userCol="user_id",  # Cambia "userID" por "user_id"
    itemCol="artist_id",  # Cambia "artistID" por "artist_id"
    ratingCol="play_count",  # Cambia "weight" por "play_count" (o el campo que uses para las interacciones)
    coldStartStrategy="drop",
    nonnegative=True,
    implicitPrefs=True,
    rank=10,
    maxIter=10,
    regParam=0.1
    )
    model = als.fit(df)

    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)
    model.save(MODEL_PATH)
    print("Modelo ALS guardado en:", MODEL_PATH)

def get_recommendations(user_id, num_items=10):
    model_trained = load_or_train_model()  # Verifica si el modelo fue entrenado
    model = ALSModel.load(MODEL_PATH)
    
    user_df = spark.createDataFrame([(user_id,)], ["user_id"])
    recommendations = model.recommendForUserSubset(user_df, num_items)
    recs = recommendations.selectExpr("explode(recommendations) as rec") \
                          .select(col("rec.artistID"), col("rec.rating"))
    
    recs_dict = recs.toPandas().to_dict(orient="records")
    
    # Agregamos un mensaje si el modelo fue entrenado automáticamente
    if model_trained:
        return {
            "message": "El modelo fue entrenado y cargado exitosamente",
            "user_id": user_id,
            "recommendations": recs_dict
        }
    else:
        return {
            "user_id": user_id,
            "recommendations": recs_dict
        }