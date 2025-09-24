import os
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

MODEL_PATH = "/app/titanic_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

# Loading the model
model = joblib.load(MODEL_PATH)

class Passenger(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    Fare: float

@app.post("/predict")
def predict(data: Passenger):
    sex = 1 if data.Sex.lower() == "female" else 0
    features = [[data.Pclass, sex, data.Age, data.Fare]]
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}
