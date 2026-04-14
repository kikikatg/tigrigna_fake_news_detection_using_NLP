import streamlit as st
import joblib
from utils.preprocessing import preprocess
import time
import base64
from datetime import datetime

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
# LOAD MODEL
# ===============================
model = joblib.load("models/svm_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


# ===============================
# LOAD IMAGE
# ===============================
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
# SIDEBAR NAVIGATION
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
        st.markdown(
            """
        <h1 style='color:#00ffcc;'>Fake News Detection</h1>
        <h4>AI-powered system for detecting REAL vs FAKE news</h4>
        <p style='color:#ccc;'>Built using NLP + Machine Learning (SVM)</p>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f'<img src="data:image/png;base64,{bg_image}" class="hero-img">',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    default_text = ""
    if st.session_state.reset_input:
        default_text = ""
        st.session_state.reset_input = False

    text = st.text_area(
        "Enter News Text:",
        value=default_text,
        height=200,
        key="input_area",
        placeholder="Enter the news here...",
    )

    st.write(f"Words: {len(text.split())} | Characters: {len(text)}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧹 Clear"):
            st.session_state.reset_input = True
            st.rerun()

    with col2:
        predict_clicked = st.button("🚀 Predict")

    if predict_clicked:

        if text.strip() == "":
            st.warning("Enter text first")

        else:
            with st.spinner("Analyzing..."):
                time.sleep(1)

                processed = preprocess(text)
                vec = vectorizer.transform([processed])
                prediction = model.predict(vec)[0]
                score = model.decision_function(vec)[0]

                confidence = abs(score)
                percentage = min(100, int(confidence * 100))

            if prediction == 1:
                result = "🟢 REAL NEWS"
                st.success(result)
                st.markdown(f"### 🟢 {percentage}% Real News")
            else:
                result = "🔴 FAKE NEWS"
                st.error(result)
                st.markdown(f"### 🔴 {percentage}% Fake News")

            # ===============================
            # CUSTOM BAR (FIXED POSITION)
            # ===============================
            if prediction == 1:
                bar_color = "#00bfff"
            else:
                bar_color = "#ff4d4d"

            st.markdown(
                f"""
            <div style='display:flex; justify-content:center; margin-top:10px;'>
                <div style='width:50%; background:#ffffff; border-radius:10px; overflow:hidden;'>
                    <div style='width:{percentage}%; background:{bar_color}; padding:8px 0; text-align:center; color:black; font-weight:bold;'>
                        {percentage}%
                    </div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.write(f"Confidence Score: {score:.2f}")

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
## 📌 Project Overview

The **Tigrigna Fake News Detection System** is an AI-powered web application designed to automatically classify news content as **REAL** or **FAKE** using Natural Language Processing (NLP) and Machine Learning.

This system focuses on **low-resource languages like Tigrigna**, where misinformation detection tools are very limited.

---

## 🎯 Objectives

- Detect fake news in Tigrigna language  
- Provide real-time classification  
- Reduce misinformation spread  
- Build an intelligent NLP-based system  

---

## 🧠 Technologies Used

### 🔹 NLP Techniques
- Text preprocessing (cleaning, normalization)
- Tokenization
- Stopword removal (custom Tigrigna stopwords)

### 🔹 Feature Extraction
- TF-IDF Vectorization

### 🔹 Machine Learning
- Naive Bayes  
- Logistic Regression  
- Support Vector Machine (Final Model)

---

## 📊 Model Performance

- Accuracy: ~96%  
- High precision and recall  
- Strong generalization  

---

## ⚙️ System Features

- Text input and analysis  
- Real-time prediction  
- Confidence visualization  
- Prediction history  
- Interactive UI  

---

## 🏗️ Architecture

- Streamlit UI  
- ML Model (SVM)  
- Preprocessing pipeline  

---

## 🚀 Future Improvements

- Convert to full-stack (React + FastAPI)  
- Add deep learning (LSTM / Transformers)  
- Expand dataset  
- API integration  

---

## 💡 Impact

This project demonstrates how AI can be applied to:
- Fight misinformation  
- Support local languages  
- Build real-world intelligent systems  

---

## 🔗 GitHub

👉 https://github.com/kikikatg/tigrigna_fake_news_detection_using_NLP
"""
    )

# ===============================
# FOOTER
# ===============================
st.markdown("---")

st.markdown(
    """
<div style='text-align:center; color:gray; font-size:14px; line-height:1.6;'>
    🚀 <b>Tigrigna Fake News Detection System</b> <br>
   Developed by <b>CSE Final Year Project Team</b> 👨‍💻👩‍💻 <br>
    Built with Streamlit, NLP & Machine Learning <br>
    © 2026 All Rights Reserved
</div>
""",
    unsafe_allow_html=True,
)
