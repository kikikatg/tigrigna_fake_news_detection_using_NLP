import re
import numpy as np

# ===============================
# STOPWORDS (CLEAN + STABLE)
# ===============================
stopwords = set(
    [
        "ኣነ",
        "ንስኻ",
        "ንስኺ",
        "ንሱ",
        "ንሳ",
        "ንሕና",
        "ንሳቶም",
        "እዚ",
        "እቲ",
        "እታ",
        "እቶም",
        "እዞም",
        "እዚኣ",
        "እቲኣ",
        "እና",
        "ወይ",
        "ግን",
        "ስለዚ",
        "እኳ",
        "እንተ",
        "እውን",
        "ኣብ",
        "ናብ",
        "ካብ",
        "ምስ",
        "ብ",
        "ን",
        "ናይ",
        "እዩ",
        "እየ",
        "እዮም",
        "ኣሎ",
        "የለን",
        "ሕጂ",
        "ቅድሚ",
        "ድሕሪ",
        "ኩሉ",
        "ሓደ",
        "ገለ",
        "መን",
        "እንታይ",
        "ኣበይ",
    ]
)

# ===============================
# SAFETY CONSTANTS
# ===============================
MIN_TOKEN_LENGTH = 2
MAX_TEXT_LENGTH = 5000


# ===============================
# TEXT CLEANING (ROBUST)
# ===============================
def clean_text(text):
    if text is None:
        return ""

    text = str(text)

    # limit extremely long inputs (prevents abuse / crashes)
    text = text[:MAX_TEXT_LENGTH]

    # remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # remove emails
    text = re.sub(r"\S+@\S+", "", text)

    # remove numbers (both latin + geez numerals)
    text = re.sub(r"[0-9\u1369-\u137C]", "", text)

    # keep only Tigrigna + spaces
    text = re.sub(r"[^\u1200-\u137F\s]", " ", text)

    # normalize spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ===============================
# NORMALIZATION (SAFE VERSION)
# ===============================
def normalize_tigrigna(text):
    if not text:
        return ""

    replacements = {
        "አ": "ኣ",
        "ዐ": "ኣ",
        "ሐ": "ሀ",
        "ኀ": "ሀ",
        "ሓ": "ሀ",
        "ሸ": "ሠ",
        "ጸ": "ፀ",
        "፡": " ",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


# ===============================
# TOKENIZATION (STRICT + CLEAN)
# ===============================
def tokenize(text):
    if not text:
        return []

    # ONLY Tigrigna tokens (no English leakage)
    tokens = re.findall(r"[ሀ-፿]+", text)

    return tokens


# ===============================
# TOKEN CLEANING
# ===============================
def clean_tokens(tokens):
    if not tokens:
        return []

    cleaned = []
    for t in tokens:
        if t not in stopwords and len(t) >= MIN_TOKEN_LENGTH:
            cleaned.append(t)

    return cleaned


# ===============================
# MAIN PREPROCESS PIPELINE
# ===============================
def preprocess(text, return_tokens=False):
    """
    Production-safe preprocessing function.
    MUST behave same in training and inference.
    """

    text = clean_text(text)
    text = normalize_tigrigna(text)

    tokens = tokenize(text)
    tokens = clean_tokens(tokens)

    # safety fallback (VERY IMPORTANT for deployment)
    if len(tokens) == 0:
        return [] if return_tokens else ""

    if return_tokens:
        return tokens

    return " ".join(tokens)


# ===============================
# DEBUG FUNCTION (OPTIONAL)
# ===============================
def debug_preprocess(text):
    print("RAW:", text)
    cleaned = clean_text(text)
    print("CLEAN:", cleaned)

    normalized = normalize_tigrigna(cleaned)
    print("NORMALIZED:", normalized)

    tokens = tokenize(normalized)
    print("TOKENS:", tokens)

    final = clean_tokens(tokens)
    print("FINAL:", final)

    return final
