from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from .database import Base


# =========================================
# PREDICTION HISTORY TABLE
# =========================================
class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)

    text = Column(String, nullable=False)

    label = Column(String, nullable=False)

    confidence = Column(Float, nullable=False)

    risk_level = Column(String, nullable=False)

    source_pattern = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.now)
