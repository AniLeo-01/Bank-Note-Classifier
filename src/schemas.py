from pydantic import BaseModel

class CreatePredictionRequest(BaseModel):
    prediction_label: str
    prediction_score : float

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
