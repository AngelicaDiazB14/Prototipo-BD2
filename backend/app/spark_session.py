from pyspark.sql import SparkSession

def get_spark_session(app_name="MusicRecommenderApp"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "8") \
        .getOrCreate()
    return spark
