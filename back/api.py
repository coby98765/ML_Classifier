# lib's
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
# classes
from back.trainer import Trainer
from back.tester import Test
from back.predictor import Predictor


class TrainJSON(BaseModel):
    name: str
    file: str

app = FastAPI()

@app.get("/")
def get_root():
    return {'Hello':'World'}

@app.post("/train/")
async def train_model(data: TrainJSON):

    return {"message": "Item created successfully", "item": data.name}

