from sqlalchemy import Column
from sqlalchemy import Integer, String, Float, DATETIME
from .db import Base


class History(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    prediction_label = Column(String, nullable=False)
    prediction_score = Column(Float, nullable=False)
    