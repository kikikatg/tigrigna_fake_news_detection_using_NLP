from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import os

# =========================
# LOAD MODEL
# =========================
MODEL_PATH = os.path.join("..", "models", "pipeline.pkl")
model = joblib.load(MODEL_PATH)

# =========================
# APP INIT
# =========================
app = FastAPI()

# =========================
# CORS (React connection)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# REQUEST FORMAT
# =========================
class NewsRequest(BaseModel):
    text: str


# =========================
# PREDICT ENDPOINT
# =========================
@app.post("/predict")
def predict_news(request: NewsRequest):
    text = request.text

    # prediction
    pred = model.predict([text])[0]

    # confidence (SVM decision function)
    try:
        score = model.decision_function([text])[0]
        confidence = float(1 / (1 + np.exp(-score))) * 100
    except:
        confidence = 50.0

    return {
        "label": "REAL" if pred == 1 else "FAKE",
        "confidence": round(confidence, 2),
    }


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {"message": "Fake News API is running"}
