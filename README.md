# 🧠 Tigrigna Fake News Detection System

## 📌 Project Overview

The **Tigrigna Fake News Detection System** is an AI-powered full-stack web application developed to automatically classify Tigrigna news content as **REAL** or **FAKE** using **Natural Language Processing (NLP)** and **Machine Learning**.

The system was developed as a **final-year Computer Science and Engineering team project** to help combat the increasing spread of misinformation in low-resource languages such as **Tigrigna**.

The application uses:
- ⚛️ **React + Vite** for the frontend
- ⚡ **FastAPI** for the backend API
- 🧠 **Machine Learning (SVM)** for prediction
- 🗄️ **SQLite + SQLAlchemy** for prediction history storage
- ☁️ **Vercel + Render** for deployment

---

# 🎯 Objectives

- Detect fake news written in Tigrigna language
- Build an intelligent automated fake news classification system
- Reduce misinformation spread through AI-based analysis
- Provide a fast, responsive, and user-friendly web application
- Store and manage prediction history

---

# 🚀 Features

- 📰 Real-time fake news prediction
- 🤖 Machine Learning classification (REAL / FAKE)
- 📊 Confidence score display
- ⚠️ Risk level analysis
- 🧾 Source pattern identification
- 🕒 Prediction history with timestamps
- 🗑️ Clear history functionality
- 🎨 Modern responsive React UI
- ⚡ FastAPI backend API integration
- ☁️ Full-stack cloud deployment
- 🔒 CORS-enabled secure API communication

---

# 🧠 Technologies Used

## 🔹 Frontend

- React.js
- Vite
- Axios
- CSS / Responsive UI

## 🔹 Backend

- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite

## 🔹 Machine Learning & NLP

- Scikit-learn
- Pandas
- NumPy
- Joblib

### NLP Techniques

- Text cleaning
- Normalization
- Tokenization
- Stopword removal

### Feature Extraction

- **TF-IDF Vectorization**

### Machine Learning Models Tested

- Naive Bayes
- Logistic Regression
- **Support Vector Machine (SVM) – Final Model**

✅ The SVM model was selected due to its strong accuracy and overall performance.

---

# 📊 Model Performance

| Metric | Score |
|--------|--------|
| Accuracy | ~96% |
| Precision | High |
| Recall | High |
| F1-Score | High |

### Evaluation Methods

- Confusion Matrix
- Cross-validation
- Classification report

---

# 🏗️ System Architecture

```text
Frontend (React + Vite)
            ↓
Axios API Requests
            ↓
FastAPI Backend
            ↓
NLP Preprocessing
            ↓
TF-IDF Vectorization
            ↓
SVM Model Prediction
            ↓
Prediction Result + Confidence
            ↓
Database Storage (SQLite)

## 🔗 GitHub Repository

👉 [View Source Code](https://github.com/kikikatg/tigrigna_fake_news_detection_using_NLP)

---

# 🌐 Live Application Links

## 🔹 Frontend Application (Vercel)

👉 [Open Frontend App](https://tigrigna-fake-news-detection-using.vercel.app/)

---

## 🔹 Backend API (Render)

👉 [Open Backend API](https://tigrigna-fake-news-detection-using-nlp-1.onrender.com)

---

## 🤖 Telegram Bot

👉 [Chat with the Bot](https://t.me/tigrigna_fake_news_detector_bot)