from fastapi import FastAPI
import mlflow.pyfunc
from pydantic import BaseModel
import pandas as pd

app =FastAPI()

mlflow.set_tracking_uri(uri='http://127.0.0.1:5000')

# Load model from model registry
model = mlflow.pyfunc.load_model("models:/Best Random Forest Regressor@latest")

#input Schema

class HouseInput(BaseModel):
    MedInc: float
    HouseAge: float    
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def home():
    return {"status": "API running"}

@app.get("/health")
def health():
    return {"status": "Healthy"}

@app.post("/predict")
def predict(data: HouseInput):
    try:
        df = pd.DataFrame([data.model_dump()])
        pred =model.predict(df)

        return {
            "prediction": float(pred[0])
        }

    except Exception as e:
        return {"error": str(e)}