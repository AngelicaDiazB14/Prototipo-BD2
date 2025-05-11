import pandas as pd
import os

# Rutas
dataset_path = "./app/data"
parquet_output_path = "./app/parquet"

# Crear carpeta de salida si no existe
os.makedirs(parquet_output_path, exist_ok=True)

# Archivos y sus columnas
files_info = {
    "artists.dat": ["artist_id", "name", "url", "picture_url"],
    "tags.dat": ["tag_id", "tag_value"],
    "user_artists.dat": ["user_id", "artist_id", "play_count"],
    "user_taggedartists.dat": ["user_id", "artist_id", "tag_id", "day", "month", "year"],
    "user_taggedartists-timestamps.dat": ["user_id", "artist_id", "tag_id", "timestamp"],
    "user_friends.dat": ["user_id", "friend_id"]
}

# Convertir .dat a .parquet
for filename, columns in files_info.items():
    file_path = os.path.join(dataset_path, filename)
    try:
        df = pd.read_csv(file_path, sep="\t", names=columns, header=0)
        parquet_file = os.path.join(parquet_output_path, filename.replace(".dat", ".parquet"))
        df.to_parquet(parquet_file, index=False)
        print(f"Convertido: {filename} → {parquet_file}")
    except Exception as e:
        print(f"Error procesando {filename}: {e}")
