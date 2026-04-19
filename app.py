import streamlit as st
import joblib
from utils.preprocessing import preprocess
import base64
from datetime import datetime
import numpy as np
import os

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="wide")

# ===============================
# SESSION STATE
# ===============================
if "history" not in st.session_state:
    st.session_state.history = []

if "page" not in st.session_state:
    st.session_state.page = "home"


# ===============================
# LOAD PIPELINE
# ===============================
def load_pipeline():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    pipeline_path = os.path.join(BASE_DIR, "models", "pipeline.pkl")
    return joblib.load(pipeline_path)


pipeline = load_pipeline()


# ===============================
# LOAD IMAGE (HERO IMAGE)
# ===============================
@st.cache_data
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


hero_image = get_base64("assets/ui-background.png")

# ===============================
# CSS (NO BACKGROUND IMAGE HERE)
# ===============================
st.markdown(
    """
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}

.sidebar-box {
    background: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #333;
}

.hero-img {
    width: 100%;
    border-radius: 12px;
}

textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 8px !important;
    padding: 10px !important;
}

div.stButton > button {
    background-color: #00ffcc;
    color: black;
    font-weight: bold;
    border-radius: 8px;
}

.history-box {
    background: #1c1f26;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ===============================
# SIDEBAR
# ===============================
st.sidebar.markdown('<div class="sidebar-box">', unsafe_allow_html=True)

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "home"

if st.sidebar.button("ℹ️ About"):
    st.session_state.page = "about"

if st.sidebar.button("📜 History"):
    st.session_state.page = "history"

st.sidebar.markdown("</div>", unsafe_allow_html=True)

# ===============================
# HOME PAGE
# ===============================
if st.session_state.page == "home":

    # HERO SECTION
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(
            """
            <h1 style='color:#00ffcc;'>Fake News Detection</h1>
            <h4>AI-powered system for detecting REAL vs FAKE news</h4>
            <p style='color:#ccc;'>
                Built using Natural Language Processing and Machine Learning (SVM + TF-IDF)
            </p>
            <hr>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f'<img src="data:image/png;base64,{hero_image}" class="hero-img">',
            unsafe_allow_html=True,
        )

    # ===============================
    # INPUT AREA
    # ===============================
    text = st.text_area(
        "Enter News Text:", height=200, placeholder="Type or paste news here..."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧹 Clear"):
            st.rerun()

    with col2:
        predict_clicked = st.button("🚀 Predict")

    # ===============================
    # PREDICTION LOGIC
    # ===============================
    if predict_clicked:

        if text.strip() == "":
            st.warning("Please enter text first")

        else:
            with st.spinner("Analyzing..."):

                processed = preprocess(text)

                prediction = pipeline.predict([processed])[0]

                vectorized = pipeline.named_steps["vectorizer"].transform([processed])
                raw_score = pipeline.named_steps["model"].decision_function(vectorized)[
                    0
                ]

                probability = 1 / (1 + np.exp(-raw_score))
                percentage = int(probability * 100)

                score = raw_score

                if prediction == 1:
                    result = "🟢 REAL NEWS"
                    confidence = percentage
                    st.success(result)
                else:
                    result = "🔴 FAKE NEWS"
                    confidence = 100 - percentage
                    st.error(result)

                st.markdown(f"### Confidence: {confidence}%")

                st.progress(confidence / 100)

                st.write(f"Score: {score:.2f}")

                st.session_state.history.append(
                    {
                        "text": text[:200],
                        "result": result,
                        "score": score,
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                )

# ===============================
# HISTORY PAGE
# ===============================
elif st.session_state.page == "history":

    col1, col2 = st.columns([4, 1])

    with col1:
        st.title("📜 Prediction History")

    with col2:
        if st.button("🗑 Delete All"):
            st.session_state.history = []
            st.rerun()

    if not st.session_state.history:
        st.info("No history yet")
    else:
        for item in reversed(st.session_state.history):
            st.markdown(
                f"""
                <div class="history-box">
                    <b>Text:</b> {item['text']}<br>
                    <b>Result:</b> {item['result']}<br>
                    <b>Score:</b> {item['score']:.2f}<br>
                    <b>Time:</b> {item['time']}
                </div>
                """,
                unsafe_allow_html=True,
            )

# ===============================
# ABOUT PAGE
# ===============================
elif st.session_state.page == "about":

    st.title("ℹ️ About This Project")

    st.markdown(
        """
### 🧠 Tigrigna Fake News Detection System

This system detects whether a news article is REAL or FAKE using Machine Learning.

---

### 🎯 Features
- Real-time prediction
- NLP preprocessing
- SVM classification model
- Prediction history

---

### ⚙️ Tech Stack
- Python
- Streamlit
- Scikit-learn (SVM + TF-IDF)

---

### 👨‍💻 Developer
Kiros Asefa
"""
    )
