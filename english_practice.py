# ===============================
# English Fake News Practice Script
# ===============================

# STEP 1: Import Libraries
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# STEP 2: Load Datasets
fake = pd.read_csv("datasets/Fake.csv")
true = pd.read_csv("datasets/True.csv")

# Add labels
fake["label"] = 1   # 1 = Fake
true["label"] = 0   # 0 = Real

# Combine datasets
df = pd.concat([fake, true], axis=0)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print("✅ Dataset loaded successfully!")
print(df["label"].value_counts())
print(df.head())

# STEP 3: Clean Text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)        # remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)   # remove punctuation
    text = re.sub(r"\s+", " ", text)          # remove extra spaces
    return text

df["clean_text"] = df["text"].apply(clean_text)

print("✅ Text cleaning completed!")

# STEP 4: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    df["clean_text"], df["label"], test_size=0.2, random_state=42
)

print("✅ Train/Test split completed!")
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

# STEP 5: TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("✅ TF-IDF vectorization completed!")

# ===============================
# STEP 8: Train Logistic Regression
# ===============================
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

print("✅ Logistic Regression model training completed!")

# ===============================
# STEP 9: Evaluate Model
# ===============================
y_pred = model.predict(X_test_tfidf)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# AUC Score
y_prob = model.predict_proba(X_test_tfidf)[:,1]
print("\nAUC Score:", roc_auc_score(y_test, y_prob))