import os
import joblib
import numpy as np

from utils.preprocessing import preprocess

# =========================================
# LOAD MODEL PIPELINE
# =========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "models",
    "pipeline.pkl",
)

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
        raise ValueError("Please enter meaningful news text.")

    # =====================================
    # PREPROCESS
    # =====================================
    processed_text = preprocess(raw_text)

    if processed_text == "":
        raise ValueError("Text became empty after preprocessing.")

    # =====================================
    # VECTORIZE
    # =====================================
    vectorized = vectorizer.transform([processed_text])

    # =====================================
    # PREDICT
    # =====================================
    prediction = model.predict(vectorized)[0]

    probabilities = model.predict_proba(vectorized)[0]

    confidence = float(np.max(probabilities) * 100)

    # =====================================
    # LABEL
    # =====================================
    label = "REAL" if prediction == 1 else "FAKE"

    # =====================================
    # RISK LEVEL
    # =====================================
    if confidence >= 85:
        risk_level = "LOW"

    elif confidence >= 60:
        risk_level = "MEDIUM"

    else:
        risk_level = "HIGH"

    # =====================================
    # SOURCE PATTERN
    # =====================================
    source_pattern = "Unknown"

    lowered = raw_text.lower()

    if "reuters" in lowered or "ሮይተርስ" in lowered:
        source_pattern = "Reuters-like"

    elif "cnn" in lowered:
        source_pattern = "CNN-like"

    elif "bbc" in lowered:
        source_pattern = "BBC-like"

    # =====================================
    # RESPONSE
    # =====================================
    return {
        "label": label,
        "confidence": round(confidence, 2),
        "risk_level": risk_level,
        "source_pattern": source_pattern,
        "processed_text": processed_text,
        "model_used": "Logistic Regression + TF-IDF",
    }
