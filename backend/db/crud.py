from sqlalchemy.orm import Session

from .models import PredictionHistory


# =========================================
# SAVE PREDICTION
# =========================================
def save_prediction(
    db: Session,
    text: str,
    label: str,
    confidence: float,
    risk_level: str,
    source_pattern: str,
):

    prediction = PredictionHistory(
        text=text,
        label=label,
        confidence=confidence,
        risk_level=risk_level,
        source_pattern=source_pattern,
    )

    db.add(prediction)

    db.commit()

    db.refresh(prediction)

    return prediction


# =========================================
# GET HISTORY
# =========================================
def get_history(db: Session):

    return (
        db.query(PredictionHistory).order_by(PredictionHistory.created_at.desc()).all()
    )


# =========================================
# CLEAR HISTORY
# =========================================
def clear_history(db: Session):

    db.query(PredictionHistory).delete()

    db.commit()
