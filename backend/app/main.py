from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.recommender import get_recommendations, train_and_save_model

app = FastAPI()

# CORS para permitir Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API de recomendaciones de música"}

@app.get("/api/recommend/{user_id}")
def recommend(user_id: int):
    try:
        recs = get_recommendations(user_id)
        return {"user_id": user_id, "recommendations": recs}
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/train")
def train_model():
    train_and_save_model()
    return {"message": "✅ Modelo entrenado y guardado"}
