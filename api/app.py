from api.loggingut import init_db, log_prediction
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("model/model.pkl")
app = FastAPI()

class InputData(BaseModel):
    sl: float
    sw: float
    pl: float
    pw: float

@app.get("/")
def root():
    return {"message": "Model is up"}

@app.on_event("startup")
def startup_event():
    init_db()

@app.post("/predict")
def get_prediction(data: InputData):
    x = np.array([[data.sl, data.sw, data.pl, data.pw]])
    y = model.predict(x)[0]
    log_prediction(data.sl, data.sw, data.pl, data.pw, int(y))
    return {"prediction": int(y)}
