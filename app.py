from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import pandas as pd

app = FastAPI(title="Simple ML API")

try:
    model = load('model.joblib')
except FileNotFoundError:
    model = None

class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"status": "ok", "message": "ML API is running!"}

@app.post("/predict")
def predict(data: InputData):
    if model is None:
        return {"error": "Model not found. Please train the model first."}
        
    input_df = pd.DataFrame([data.dict()])
    
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    return {
        "prediction": prediction[0],
        "probability_setosa": float(probability[0][0]),
        "probability_versicolor": float(probability[0][1]),
        "probability_virginica": float(probability[0][2])
    }