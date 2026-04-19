import streamlit as st
import joblib
from utils.preprocessing import preprocess
import time
import base64
from datetime import datetime
import os
import numpy as np

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

if "reset_input" not in st.session_state:
    st.session_state.reset_input = False


# ===============================
# LOAD PIPELINE (FIXED)
# ===============================
def load_pipeline():
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    pipeline_path = os.path.join(BASE_DIR, "models", "pipeline.pkl")

    pipeline = joblib.load(pipeline_path)

    return pipeline


pipeline = load_pipeline()


# ===============================
# LOAD IMAGE
# ===============================
@st.cache_data
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


bg_image = get_base64("assets/ui-background.png")

# ===============================
# CSS
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
    border-radius: 10px;
}

textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 8px !important;
    padding: 10px !important;
    caret-color: black !important;
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

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("...")

    with col2:
        st.markdown("...")

    st.markdown("---")

    text = st.text_area(
    "Enter News Text:",
    height=200,
    placeholder="Enter the news here..."
)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧹 Clear"):
            st.session_state.reset_input = True
            st.rerun()

    with col2:
        predict_clicked = st.button("🚀 Predict")

    # ✅ FIX: move prediction HERE
    if predict_clicked:

    if text.strip() == "":
        st.warning("Enter text first")

    else:
        with st.spinner("Analyzing..."):
            processed = preprocess(text)

            prediction = pipeline.predict([processed])[0]

            vectorized = pipeline.named_steps["vectorizer"].transform([processed])
            raw_score = pipeline.named_steps["model"].decision_function(vectorized)[0]

            probability = 1 / (1 + np.exp(-raw_score))
            percentage = int(probability * 100)

            score = raw_score  # ✅ FIXED

            if prediction == 1:
                result = "🟢 REAL NEWS"
                display_percentage = percentage
                st.success(result)
                st.markdown(f"### 🟢 {display_percentage}% Confidence (Real)")
            else:
                result = "🔴 FAKE NEWS"
                display_percentage = 100 - percentage
                st.error(result)
                st.markdown(f"### 🔴 {display_percentage}% Confidence (Fake)")

            # Progress bar
            bar_color = "#00bfff" if prediction == 1 else "#ff4d4d"

            st.markdown(
                f"""
                <div style='display:flex; justify-content:center; margin-top:10px;'>
                    <div style='width:50%; background:#ffffff; border-radius:10px; overflow:hidden;'>
                        <div style='width:{display_percentage}%; background:{bar_color}; padding:8px 0; text-align:center; color:black; font-weight:bold;'>
                            {display_percentage}%
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write(f"Confidence Score: {score:.2f}")

            # Save history
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

    if len(st.session_state.history) == 0:
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

This project is an AI-powered web application designed to classify news content as **REAL** or **FAKE** using Natural Language Processing and Machine Learning.

---

### 🎯 Key Features
- Real-time fake news detection
- Supports Tigrigna language
- Interactive and user-friendly interface
- Confidence score visualization
- Prediction history tracking

---

### ⚙️ Technologies
- **Machine Learning:** Support Vector Machine (SVM)
- **Text Processing:** TF-IDF Vectorization
- **Frontend:** Streamlit
- **Backend Logic:** Python

---

### 📊 Model Performance
- Accuracy: **~96%**
- Optimized using cross-validation
- Balanced classification for real-world data

---

### 🚀 Future Improvements
- Full-stack upgrade (React + FastAPI)
- Deep learning models (LSTM / Transformers)
- API deployment

---

### 👨‍💻 Developer
**Kiros Asefa**  
Computer Science & Engineering Student  
Mekelle University

---

### 🔗 GitHub
https://github.com/kikikatg/tigrigna_fake_news_detection_using_NLP
"""
)
# ===============================
# FOOTER
# ===============================
st.markdown(
    """
<hr>
<div style='text-align:center; color:gray; font-size:14px;'>
    🚀 <b>Tigrigna Fake News Detection System</b><br>
    Built with ❤️ using NLP & Machine Learning<br>
    © 2026 Kiros Asefa
</div>
""",
    unsafe_allow_html=True,
)
