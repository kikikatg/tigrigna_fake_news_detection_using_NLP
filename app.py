import streamlit as st
import joblib
from utils.preprocessing import preprocess
import time
import base64
from datetime import datetime

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide"
)

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
st.markdown(f"""
<style>
.stApp {{
    background-color: #0e1117;
    color: white;
}}

.sidebar-box {{
    background: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #333;
}}

.hero-img {{
    width: 100%;
    border-radius: 10px;
}}

textarea {{
    background-color: #1c1f26 !important;
    color: white !important;
}}

div.stButton > button {{
    background-color: #00ffcc;
    color: black;
    font-weight: bold;
    border-radius: 8px;
}}

.history-box {{
    background: #1c1f26;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}}
</style>
""", unsafe_allow_html=True)

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

st.sidebar.markdown('</div>', unsafe_allow_html=True)

# ===============================
# HOME PAGE
# ===============================
if st.session_state.page == "home":

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <h1 style='color:#00ffcc;'>Fake News Detection</h1>
        <h4>AI-powered system for detecting REAL vs FAKE news</h4>
        <p style='color:#ccc;'>Built using NLP + Machine Learning (SVM)</p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(
            f'<img src="data:image/png;base64,{bg_image}" class="hero-img">',
            unsafe_allow_html=True
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
        key="input_area"
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

            if prediction == 1:
                result = "🟢 REAL NEWS"
                st.success(result)
            else:
                result = "🔴 FAKE NEWS"
                st.error(result)

            st.write(f"Confidence Score: {score:.2f}")

            st.session_state.history.append({
                "text": text[:200],
                "result": result,
                "score": score,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

# ===============================
# HISTORY PAGE
# ===============================
elif st.session_state.page == "history":

    col1, col2 = st.columns([4,1])

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
            st.markdown(f"""
            <div class="history-box">
                <b>Text:</b> {item['text']}<br>
                <b>Result:</b> {item['result']}<br>
                <b>Score:</b> {item['score']:.2f}<br>
                <b>Time:</b> {item['time']}
            </div>
            """, unsafe_allow_html=True)

# ===============================
# ABOUT PAGE (FIXED)
# ===============================
elif st.session_state.page == "about":
  st.title("ℹ️ About This Project")
  st.markdown("""
## 📌 Project Overview

The **Tigrigna Fake News Detection System** is an AI-powered web application developed to automatically classify news content as **REAL** or **FAKE** using Natural Language Processing (NLP) and Machine Learning techniques.

This project was developed as a **final-year Computer Science and Engineering team project**, with the goal of addressing the growing problem of misinformation in digital media, especially in low-resource languages like Tigrigna.

---

## 🎯 Objectives

- Detect and classify fake news in Tigrigna language  
- Build an intelligent and automated text classification system  
- Reduce misinformation spread in digital platforms  
- Provide a simple and interactive user interface for real-time prediction  

---

## 🧠 Technologies & Methods Used

### 🔹 Natural Language Processing (NLP)
- Text cleaning and normalization (Tigrigna-specific preprocessing)
- Tokenization
- Stopword removal

### 🔹 Feature Extraction
- **TF-IDF (Term Frequency - Inverse Document Frequency)**
- Used to convert textual data into numerical vectors

### 🔹 Machine Learning Models
We trained and compared multiple models:
- Naive Bayes  
- Logistic Regression  
- **Support Vector Machine (SVM) – Final Selected Model**

The SVM model was selected due to its **highest accuracy and strong generalization performance**.

---

## 📊 Model Performance

- Accuracy: ~96%  
- Evaluated using:
  - Confusion Matrix  
  - Precision, Recall, F1-score  
  - Cross-validation  

The model demonstrates strong ability to distinguish between real and fake news.

---

## 💻 System Features

- 📰 Real-time news prediction  
- 🧠 AI-based classification (REAL / FAKE)  
- 📊 Confidence score display  
- 🕒 Prediction history tracking with timestamps  
- 🎨 Interactive and modern user interface  
- 🧹 Clear input and reset functionality  

---

## 🏗️ System Architecture

The system consists of:

- **Frontend + Backend (Streamlit)**  
- **Machine Learning Model (Linear SVM)**  
- **Preprocessing Module (Custom NLP pipeline)**  

All components are integrated into a single web application for simplicity and efficiency.

---

## 🚀 Future Improvements

- Deploy as a full-stack application (React + FastAPI)  
- Add multilingual support  
- Improve dataset size and diversity  
- Integrate deep learning models (e.g., LSTM, Transformers)  
- Enable API access for external systems  

---

## 👨‍💻 Development Team

This project was developed collaboratively as part of a final-year academic project.

---

## 🔗 GitHub Repository

Explore the full project code here:  
👉 https://github.com/kikikatg/tigrigna_fake_news_detection_using_NLP

---

## 📌 Conclusion

This system demonstrates how AI can be applied to solve real-world problems like fake news detection, especially in underrepresented languages. It provides a strong foundation for future research and real-world deployment.

""")
# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("Model: Linear SVM | Accuracy: ~96%")