from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# =========================================
# DATABASE URL
# =========================================
import os

# Get project root (Final_Project)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'fake_news.db')}"

# =========================================
# ENGINE
# =========================================
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# =========================================
# SESSION
# =========================================
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# =========================================
# BASE
# =========================================
Base = declarative_base()
