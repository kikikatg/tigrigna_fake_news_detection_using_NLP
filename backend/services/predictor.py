import os
import joblib
import numpy as np
from utils.preprocessing import preprocess

# =========================================
# LOAD MODEL PIPELINE
# =========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "..", "models", "pipeline.pkl")

pipeline = joblib.load(MODEL_PATH)

model = pipeline.named_steps["model"]
vectorizer = pipeline.named_steps["vectorizer"]

print("✅ Model loaded:", type(model))
print("✅ Vectorizer loaded:", type(vectorizer))


# =========================================
# MAIN PREDICTION FUNCTION
# =========================================
def predict_news(raw_text: str):

    if not raw_text or len(raw_text.strip()) < 20:
        return {"success": False, "error": "Please enter meaningful news text"}

    processed_text = preprocess(raw_text)

    if processed_text == "":
        return {"success": False, "error": "Text became empty after preprocessing"}

    vectorized = vectorizer.transform([processed_text])

    prediction = model.predict(vectorized)[0]
    probabilities = model.predict_proba(vectorized)[0]

    confidence = float(np.max(probabilities) * 100)

    label = "REAL" if prediction == 1 else "FAKE"

    risk_level = "LOW" if confidence >= 85 else "MEDIUM" if confidence >= 60 else "HIGH"

    source_pattern = "Unknown"

    lowered = raw_text.lower()

    if "reuters" in lowered or "ሮይተርስ" in lowered:
        source_pattern = "Reuters-like"
    elif "cnn" in lowered:
        source_pattern = "CNN-like"
    elif "bbc" in lowered:
        source_pattern = "BBC-like"

    return {
        "label": label,
        "confidence": round(confidence, 2),
        "risk_level": risk_level,
        "source_pattern": source_pattern,
        "processed_text": processed_text,
        "model_used": "Logistic Regression + TF-IDF",
    }
