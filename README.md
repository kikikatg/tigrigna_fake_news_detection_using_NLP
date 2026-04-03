# 🧠 Tigrigna Fake News Detection System

## 📌 Project Overview

The **Tigrigna Fake News Detection System** is an AI-powered web application developed to automatically classify news content as **REAL** or **FAKE** using **Natural Language Processing (NLP)** and **Machine Learning**.

This project was built as a **final-year Computer Science and Engineering team project** to address the growing problem of misinformation, especially in **low-resource languages like Tigrigna**.

---

## 🎯 Objectives

- Detect fake news in Tigrigna language
- Build an intelligent automated classification system
- Reduce misinformation spread
- Provide an easy-to-use web interface for users

---

## 🚀 Features

- 📰 Real-time news prediction
- 🤖 Machine Learning classification (REAL / FAKE)
- 📊 Confidence score display
- 🕒 Prediction history with timestamps
- 🎨 Modern and interactive UI (Streamlit)
- 🧹 Clear input functionality

---

## 🧠 Technologies Used

### 🔹 Natural Language Processing (NLP)

- Text cleaning and normalization
- Tokenization
- Stopword removal

### 🔹 Feature Extraction

- **TF-IDF (Term Frequency – Inverse Document Frequency)**

### 🔹 Machine Learning Models

- Naive Bayes
- Logistic Regression
- **Support Vector Machine (SVM) – Final Model**

✔ The SVM model was selected due to its **high accuracy and strong performance**.

---

## 📊 Model Performance

- ✅ Accuracy: ~96%
- 📈 Evaluation Metrics:
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix

- 🔁 Cross-validation used for model reliability

---

## 💻 System Architecture

```
User Input (Text)
        ↓
Preprocessing (NLP)
        ↓
TF-IDF Vectorization
        ↓
SVM Model Prediction
        ↓
Output (REAL / FAKE + Score)
```

---

## 🖥️ User Interface

The system is built using **Streamlit**, providing:

- Interactive UI
- Fast predictions
- Simple deployment

---

## 📂 Project Structure

```
Final_Project/
│── app.py
│── models/
│   ├── svm_model.pkl
│   ├── vectorizer.pkl
│
│── utils/
│   └── preprocessing.py
│
│── assets/
│   └── ui-background.png
│
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/kikikatg/tigrigna_fake_news_detection_using_NLP.git
cd tigrigna_fake_news_detection_using_NLP
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The application can be deployed using:

- Streamlit Cloud
- Render / Railway
- Future: React + FastAPI

---

## 🔮 Future Improvements

- 🌍 Multi-language support
- 🧠 Deep Learning models (LSTM, Transformers)
- ☁️ Full-stack deployment (React + FastAPI)
- 📱 Mobile-friendly UI

---

## 👨‍💻 Team Contribution

This project was developed collaboratively as part of a final-year academic project.

---

## 🔗 GitHub Repository

👉 https://github.com/kikikatg/tigrigna_fake_news_detection_using_NLP

---

## 📌 Conclusion

This project demonstrates how **AI and NLP** can be used to solve real-world problems like fake news detection, especially in underrepresented languages. It provides a strong foundation for further research and real-world deployment.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
