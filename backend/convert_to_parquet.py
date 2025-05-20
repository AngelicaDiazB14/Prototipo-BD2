# Importa la librería pandas para manipulación de datos
import pandas as pd

# Importa Path de la biblioteca pathlib para trabajar con rutas de archivos de forma flexible
from pathlib import Path

# Define la ruta base apuntando al directorio backend/app/data de forma dinámica
base_path = Path(__file__).resolve().parent / "app" / "data"

# Diccionario con los nombres de los archivos .dat y las columnas correspondientes para cada uno
files_info = {
    "artists.dat": ["id", "name", "url", "pictureURL"],
    "tags.dat": ["tagID", "tagValue"],
    "user_artists.dat": ["userID", "artistID", "weight"],
    "user_friends.dat": ["userID", "friendID"],
    "user_taggedartists.dat": ["userID", "artistID", "tagID", "day", "month", "year"],
    "user_taggedartists-timestamps.dat": ["userID", "artistID", "tagID", "timestamp"],
}

# Itera sobre cada archivo y sus columnas definidas en el diccionario
for filename, columns in files_info.items():
    # Construye la ruta completa al archivo .dat
    file_path = base_path / filename

    # Define la ruta de salida para el archivo convertido a formato Parquet
    parquet_path = base_path / (filename.replace(".dat", ".parquet"))

    # Muestra en consola el nombre del archivo que está siendo convertido
    print(f"Convirtiendo {filename} a Parquet...")

    # Lee el archivo .dat como un DataFrame, usando tabulador como separador
    df = pd.read_csv(file_path, sep="\t", header=0, names=columns, encoding='latin1')

    # Guarda el DataFrame como archivo Parquet, usando el motor pyarrow
    df.to_parquet(parquet_path, index=False, engine="pyarrow")

    # Informa en consola que el archivo Parquet ha sido guardado
    print(f"Guardado: {parquet_path}")
