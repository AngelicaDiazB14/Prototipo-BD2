# Importa el objeto APIRouter de FastAPI, que permite definir rutas de forma modular
from fastapi import APIRouter

# Importa la función get_recommendations desde el módulo recommender
from app.recommender import get_recommendations

# Crea una instancia de APIRouter para agrupar rutas relacionadas
router = APIRouter()

# Define una ruta HTTP GET en la URL /recommendations/user/{user_id}
# Esta ruta acepta un parámetro entero user_id en la URL
@router.get("/recommendations/user/{user_id}")
def recommendations(user_id: int):
    # Llama a la función get_recommendations pasando el user_id como argumento
    # y retorna el resultado al cliente
    return get_recommendations(user_id)
