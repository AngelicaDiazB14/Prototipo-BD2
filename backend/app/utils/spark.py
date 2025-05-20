# Importa el módulo sys, necesario para acceder al ejecutable actual de Python
import sys

# Importa el módulo os, utilizado para gestionar variables de entorno del sistema
import os

# Importa la clase SparkSession desde PySpark, que es la entrada principal para utilizar Spark
from pyspark.sql import SparkSession

# Define una función que crea y retorna una SparkSession configurada
def get_spark_session(app_name="MusicRecommender"):
    os.environ["PYSPARK_PYTHON"] = sys.executable

    builder = SparkSession.builder\
        .appName(app_name)\
        .config("spark.executor.memory", "2g")\
        .config("spark.driver.memory", "2g")\
        .config("spark.sql.shuffle.partitions", "8")\
        .config("spark.network.timeout", "600s")\
        .config("spark.sql.legacy.timeParserPolicy", "LEGACY")\
        .config("spark.hadoop.io.native.lib.available", "false")

    if os.name == 'nt':
        builder = builder\
            .config("spark.hadoop.home.dir", "C:/winutils")\
            .config("spark.sql.warehouse.dir", "file:///C:/tmp")\
            .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem")

    return builder.getOrCreate()
