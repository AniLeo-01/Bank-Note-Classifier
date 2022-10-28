from fastapi import FastAPI, Depends
import numpy as np
import pickle
import pandas as pd
from .schemas import CreatePredictionRequest, BankNote
from .db import get_db
from sqlalchemy.orm import Session
from .models import History

app = FastAPI()

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

'''
#index page
@app.get('/')
def index():
    return {"message": "Welcome to Banknote Authentication System"}
'''

#prediction
@app.post('/predict')
def predict_banknote(data: BankNote, db: Session = Depends(get_db)):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    # 1 for Fake, 0 for Bank
    prediction_label = ""
    if(prediction[0]>0.5):
        prediction_label = "Fake Note"
    else:
        prediction_label = "Bank Note"
    create_prediction_history = History(
        prediction_label = prediction_label,
        prediction_score = prediction[0].astype(float)
    )
    db.add(create_prediction_history)
    db.commit()
    return {"Prediction": prediction_label}

@app.get('/history_by_id')
def get_history_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(History).filter(History.id == id).first()

@app.get('/history')
def get_history(db: Session = Depends(get_db)):
    yield db.query(History).all()

@app.get('/history_count')
def get_history_count(db: Session = Depends(get_db)):
    return db.query(History).count()

#delete history
@app.delete('/history_by_id')
def delete_history_by_id(id: int, db: Session = Depends(get_db)):
    deleted_history = db.query(History).filter(History.id == id).first()
    db.query(History).filter(History.id == id).delete()
    db.commit()
    return {'Deleted_element': deleted_history, 'Success': True, "Deleted_id": id}

@app.delete('/history')
def delete_history(db: Session = Depends(get_db)):
    delete_counter = db.query(History).count()
    db.query(History).delete()
    db.execute("ALTER SEQUENCE predictions_id_seq RESTART WITH 1")
    db.commit()
    return {"Deleted_records": delete_counter}
