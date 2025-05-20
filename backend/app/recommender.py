from app.utils.spark import get_spark_session
from pyspark.ml.recommendation import ALS

# Spark session
spark = get_spark_session()

# Dataset de interacciones usuario-artista
df = spark.read.parquet("backend/app/data/user_artists.parquet")
df = df.selectExpr("int(userID) as userID", "int(artistID) as artistID", "int(weight) as weight")

# Metadata de artistas (solo necesitamos ID, nombre y URL)
df_artists = spark.read.parquet("backend/app/data/artists.parquet") \
    .selectExpr("int(id) as artistID", "name", "url")

# Entrenamiento del modelo ALS
als = ALS(
    maxIter=10,
    regParam=0.1,
    userCol="userID",
    itemCol="artistID",
    ratingCol="weight",
    coldStartStrategy="drop",
    nonnegative=True
)

model = als.fit(df)

def get_recommendations(user_id: int, num_items: int = 20):
    users = spark.createDataFrame([(user_id,)], ["userID"])
    recs = model.recommendForUserSubset(users, num_items).collect()

    if not recs:
        return {"userID": user_id, "recommendations": []}

    recommendations = recs[0].recommendations
    artist_ids = [r.artistID for r in recommendations]

    # Obtener metadata básica de artistas recomendados
    artist_info = df_artists.filter(df_artists.artistID.isin(artist_ids)).collect()
    artist_map = {row.artistID: row.asDict() for row in artist_info}

    return {
        "userID": user_id,
        "recommendations": [
            {
                "artistID": r.artistID,
                "artistName": artist_map.get(r.artistID, {}).get("name", "Desconocido"),
                "rating": float(r.rating),
                "url": artist_map.get(r.artistID, {}).get("url", "")
                
            }
            for r in recommendations
        ]
    }