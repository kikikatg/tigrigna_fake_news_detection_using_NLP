import re

# ===============================
# STOPWORDS (UNCHANGED)
# ===============================
stopwords = set([
    "ኣነ","ንስኻ","ንስኺ","ንሱ","ንሳ","ንሕና","ንሳቶም","ንኣይ","ንእሱ","ንእሳ","ንእኛ","ንእኦም",
    "እዚ","እቲ","እታ","እቶም","እዞም","እዚኣ","እቲኣ",
    "እና","ወይ","ግን","ምኽንያቱ","ስለዚ","እኳ","እንተ","እንከ","እውን","ደጊም",
    "ኣብ","ናብ","ካብ","ምስ","ብዘይ","ብዛዕባ","ን","ናይ","ብ","ላዕሊ","ታሕቲ",
    "እዩ","እየ","እዮም","ነበረ","ነበሩ","ክኸውን","ኣለኒ","ኣለዎ","ኣለዋ","ኣሎ","ኣሎም",
    "ግበር","ይገብር","ገበረ","ክኽእል","ክ","ምናልባት",
    "ኣይ","የለን","ከቶ","ምንም","ዋላ","ኣይኮነን",
    "ኩሉ","ብዙሕ","ሓደ","ገለ","ዝኾነ","ነፍሲ","ወከፍ","ዝያዳ","ንእሽቶ",
    "ሕጂ","ከዚ","ቅድሚ","ድሕሪ","ግዜ",
    "ስለምንታይ","ከመይ","እንታይ","መን","ኣበይ",
    "ከም","ከምዚ","ከምኡ",
    "ስለ","ስለዚ",
    "ዝ","ዝኾነ",
    "እንተ","እንተኾነ",
    "ኣሎ","የለን",
    "ሓደ","ብዙሕ"
])

# ===============================
# CLEAN TEXT
# ===============================
def clean_text(text):
    text = str(text)

    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"[።፣፤፥፦፧፨]", "", text)
    text = re.sub(r'[.,;:!?()\[\]{}"\'`~@#$%^&*+=|\\/<>_-]', "", text)
    text = re.sub(r"[0-9\u1369-\u137C]", "", text)
    text = re.sub(r"[^\w\s\u1200-\u137F]", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()

# ===============================
# NORMALIZE TIGRIGNA
# ===============================
def normalize_tigrigna(text):
    replacements = {
        "አ": "ኣ", "ዐ": "ኣ",
        "ሐ": "ሀ", "ኀ": "ሀ", "ሓ": "ሀ",
        "ሰ": "ሠ", "ሸ": "ሠ",
        "ጸ": "ፀ",
        "ከ": "ካ", "ኸ": "ካ",
        "ዘ": "ዠ",
        "ደ": "ዳ",
        "ገ": "ጋ",
        "በ": "ባ",
        "ፐ": "ፓ",
        "ኡ": "ኢ", "ኤ": "ኢ", "እ": "ኢ", "ኦ": "ኢ",
        "፡": " "
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text

# ===============================
# TOKENIZATION
# ===============================
def tokenize(text):
    return re.findall(r"[A-Za-z]+|[ሀ-፿]+", text)

# ===============================
# REMOVE STOPWORDS
# ===============================
def clean_tokens(tokens):
    return [word for word in tokens if word not in stopwords]

# ===============================
# FINAL PREPROCESS FUNCTION
# ===============================
def preprocess(text):
    text = clean_text(text)
    text = normalize_tigrigna(text)
    tokens = tokenize(text)
    tokens = clean_tokens(tokens)
    return " ".join(tokens)