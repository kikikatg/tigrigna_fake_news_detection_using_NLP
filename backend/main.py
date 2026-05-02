from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas.news_schema import NewsRequest
from backend.services.predictor import predict_news

app = FastAPI(
    title="Tigrigna Fake News Detection API",
    version="2.0.0",
)

# =========================================
# CORS
# =========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================
# ROOT
# =========================================
@app.get("/")
def root():
    return {"message": "API Running"}


# =========================================
# HEALTH
# =========================================
@app.get("/health")
def health():
    return {"status": "ok"}


# =========================================
# PREDICT
# =========================================
@app.post("/predict")
def predict(request: NewsRequest):

    try:
        return predict_news(request.text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
