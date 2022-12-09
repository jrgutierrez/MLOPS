from fastapi import FastAPI
from pydantic import BaseModel
from model.model import __version__ as model_version
from model.model import prediction
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

class DataIn(BaseModel):
    gender: int
    height: float

class DataOut(BaseModel):
    weight: float

@app.get('/')
def index():
    status = {
        'health_check': 'OK',
        'model_version': model_version
    }
    return status

@app.post('/predict', response_model = DataOut)
def predict(data: DataIn):
    result = {
        'weight': prediction(data.gender, data.height)
    }
    return result