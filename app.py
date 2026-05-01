# =========================================
# 📰 FAKE NEWS DETECTION SYSTEM
# FINAL CLEAN DEPLOYMENT VERSION
# =========================================

import streamlit as st
import joblib
import os
import numpy as np
from datetime import datetime
from utils.preprocessing import preprocess

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="wide")

# =========================================
# SESSION STATE
# =========================================
if "history" not in st.session_state:
    st.session_state.history = []

if "page" not in st.session_state:
    st.session_state.page = "home"


# =========================================
# LOAD MODEL
# =========================================
@st.cache_resource
def load_model():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "models", "pipeline.pkl")

    if not os.path.exists(model_path):
        st.error("❌ Model file not found.")
        return None

    try:
        pipeline = joblib.load(model_path)
        return pipeline

    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return None


pipeline = load_model()

if pipeline is None:
    st.stop()

# =========================================
# CUSTOM CSS
# =========================================
st.markdown(
    """
<style>

.stApp {
    background-color: #0e1117;
    color: white;
}

/* TEXT AREA */
textarea {
    background-color: #1c1f26 !important;
    color: white !important;
    caret-color: white !important;
    border-radius: 12px !important;
    border: 1px solid #333 !important;
    font-size: 16px !important;
}

/* TEXT AREA LABEL */
label {
    color: white !important;
    font-weight: bold;
}

/* BUTTONS */
div.stButton > button {
    background-color: #00d4aa;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1rem;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #00b894;
    color: white;
}

/* HISTORY BOX */
.history-box {
    background: #1c1f26;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid #333;
}

</style>
""",
    unsafe_allow_html=True,
)

# =========================================
# SIDEBAR
# =========================================
st.sidebar.title("🧭 Navigation")

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "home"

if st.sidebar.button("📜 History"):
    st.session_state.page = "history"

if st.sidebar.button("ℹ️ About"):
    st.session_state.page = "about"

# =========================================
# HOME PAGE
# =========================================
if st.session_state.page == "home":

    st.title("📰 Fake News Detection System")

    st.markdown(
        "Detect whether a Tigrigna news article is **REAL** or **FAKE** using Machine Learning."
    )

    text = st.text_area(
        "Enter News Text",
        height=220,
        placeholder="Type or paste Tigrigna news text here...",
    )

    col1, col2 = st.columns(2)

    with col1:
        clear_btn = st.button("🧹 Clear")

    with col2:
        predict_btn = st.button("🚀 Predict")

    # CLEAR
    if clear_btn:
        st.rerun()

    # =========================================
    # PREDICTION
    # =========================================
    if predict_btn:

        if text.strip() == "":
            st.warning("⚠️ Please enter some news text.")
        else:

            with st.spinner("Analyzing news..."):

                try:

                    # PREPROCESS
                    processed = preprocess(text)

                    # MODEL + VECTORIZER
                    model = pipeline.named_steps["model"]
                    vectorizer = pipeline.named_steps["vectorizer"]

                    # VECTORIZE
                    vec = vectorizer.transform([processed])

                    # PREDICT
                    prediction = model.predict(vec)[0]

                    # PROBABILITY
                    probabilities = model.predict_proba(vec)[0]
                    confidence = float(np.max(probabilities) * 100)

                    # RESULT
                    if prediction == 1:
                        st.success("🟢 REAL NEWS")
                    else:
                        st.error("🔴 FAKE NEWS")

                    # CONFIDENCE
                    st.write(f"### Confidence: {confidence:.2f}%")
                    st.progress(confidence / 100)

                    # SAVE HISTORY
                    st.session_state.history.append(
                        {
                            "text": text[:200],
                            "result": "REAL" if prediction == 1 else "FAKE",
                            "confidence": confidence,
                            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }
                    )

                except Exception as e:
                    st.error(f"❌ Prediction Error: {str(e)}")

# =========================================
# HISTORY PAGE
# =========================================
elif st.session_state.page == "history":

    st.title("📜 Prediction History")

    if st.button("🗑 Clear History"):
        st.session_state.history = []
        st.rerun()

    if len(st.session_state.history) == 0:
        st.info("No predictions yet.")

    else:

        for item in reversed(st.session_state.history):

            st.markdown(
                f"""
            <div class="history-box">

            <b>📝 Text:</b><br>
            {item['text']}<br><br>

            <b>📌 Result:</b>
            {item['result']}<br>

            <b>🎯 Confidence:</b>
            {item['confidence']:.2f}%<br>

            <b>⏰ Time:</b>
            {item['time']}

            </div>
            """,
                unsafe_allow_html=True,
            )

# =========================================
# ABOUT PAGE
# =========================================
elif st.session_state.page == "about":

    st.title("ℹ️ About This System")

    st.markdown("""

### 🧠 Fake News Detection System

This application detects fake and real news using:

- TF-IDF Vectorization
- Logistic Regression
- Tigrigna NLP preprocessing

---

### 🚀 Features

- Real-time fake news prediction
- Confidence score estimation
- Tigrigna text preprocessing
- Prediction history
- Deployment-ready interface

---

### ⚙️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLP

---

### 📌 Note

The model was trained on dataset-based news patterns and may not perfectly generalize to all real-world news articles.

""")
