# Importa FastAPI, el framework web utilizado para construir la API
from fastapi import FastAPI
# Importa el router definido en el archivo de rutas
from app.api.routes import router
# Importa el middleware CORS para permitir comunicación entre el backend y el frontend en distintos orígenes
from fastapi.middleware.cors import CORSMiddleware
# Crea una instancia de la aplicación FastAPI con metadatos como título, versión y descripción
app = FastAPI(
    title="Song Recommender API",
    version="1.0.0",
    description="Recomendador de canciones usando Spark ALS en memoria"
)

# Agrega middleware CORS para permitir que el frontend (Angular) se comunique con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permite solicitudes desde el frontend Angular en localhost
    allow_credentials=True,  # Permite el envío de cookies/autenticación
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados en las solicitudes
)

# Incluye las rutas definidas en el router importado desde app.api.routes
app.include_router(router)
