# lib's
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
# classes
from back.predictor import Predictor
from back.flow import Flow
from back.utils import Utils

class TrainJSON(BaseModel):
    name: str
    file: str

app = FastAPI()

@app.get("/")
def get_root():
    return {'Hello':'World'}

@app.post("/train/")
async def train_model(data: TrainJSON):
    target_adr = f"./back/model_data/{data.name}_trained_data.json"
    df = Utils.get_df(data.file)
    df = Utils.clean_df(df)
    accuracy = Flow.train_and_test(df,target_adr)
    return {"item": data.name,"accuracy":accuracy}

@app.post("/predict/{model_name}")
async def train_model(model_name:str,data: dict):
    target_adr = f"./back/model_data/{model_name}_trained_data.json"
    response = Flow.predict(data,target_adr)
    return {"result": response[0],"rate":response[0]}

