import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from schemas.news_schema import NewsRequest
from services.predictor import predict_news
from db.database import SessionLocal, engine, Base
from db.crud import save_prediction, get_history, clear_history

# =========================================
# CREATE DATABASE TABLES
# =========================================
Base.metadata.create_all(bind=engine)

# =========================================
# FASTAPI
# =========================================
app = FastAPI(
    title="Tigrigna Fake News Detection API",
    version="3.0.0",
)

# =========================================
# CORS
# =========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://tigrigna-fake-news-detection-using-ahm0ms0r2-kikikatgs-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================
# DATABASE SESSION
# =========================================
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# =========================================
# ROOT
# =========================================
@app.get("/")
def root():

    return {
        "message": "API Running",
        "status": "healthy",
    }


# =========================================
# HEALTH
# =========================================
@app.get("/health")
def health():

    return {
        "status": "ok",
    }


# =========================================
# PREDICT
# =========================================
@app.post("/predict")
def predict(
    request: NewsRequest,
    db: Session = Depends(get_db),
):

    try:

        result = predict_news(request.text)

        # =================================
        # SAVE TO DATABASE
        # =================================
        save_prediction(
            db=db,
            text=request.text,
            label=result["label"],
            confidence=result["confidence"],
            risk_level=result["risk_level"],
            source_pattern=result["source_pattern"],
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =========================================
# HISTORY
# =========================================
@app.get("/history")
def history(
    db: Session = Depends(get_db),
):

    return get_history(db)


# =========================================
# CLEAR HISTORY
# =========================================
@app.delete("/history")
def delete_history(
    db: Session = Depends(get_db),
):

    clear_history(db)

    return {"message": "History cleared successfully"}
