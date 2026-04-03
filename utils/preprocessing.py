import re

stopwords = set([
    "እዚ","እዩ","እቲ","ኣብ","ናብ","ን","ናይ",
    "ከም","ስለ","ካብ","ወይ","ምስ","ነቲ","ነዚ",
    "ኣብዚ","ኝ","ይኹን","እምበር","ዋላኳ",
    "ኮታስ","ብ","እዉን","ድማ","ከሎ","እዋን",
    "ነታ","እየ","እዮም","እውን","ግን","ከምዘሎ","ኣሎ"
])

def clean_text(text):
    text = str(text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'[፡።፣፤፥፦]', '', text)
    text = re.sub(r'[^\w\sሀ-፿]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def normalize_tigrigna(text):
    text = text.replace("አ", "ኣ")
    text = text.replace("ሐ", "ሀ")
    return text

def tokenize(text):
    return re.findall(r'[A-Za-z]+|[ሀ-፿]+', text)

def clean_tokens(tokens):
    return [w for w in tokens if w not in stopwords]

def preprocess(text):
    text = clean_text(text)
    text = normalize_tigrigna(text)
    tokens = tokenize(text)
    tokens = clean_tokens(tokens)
    return " ".join(tokens)