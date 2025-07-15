# lib's
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# classes
from back.flow import Flow
from back.utils import Utils

class TrainJSON(BaseModel):
    name: str
    file: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or set specific origins
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_root():
    return {'Hello':'World'}

@app.post("/train/")
async def train_model(data: TrainJSON):
    target_adr = f"./back/model_data/{data.name}.json"
    df = Utils.get_df(data.file)
    df = Utils.clean_df(df)
    accuracy = Flow.train_and_test(df,target_adr)
    return {"item": data.name,"accuracy":accuracy}

@app.post("/predict/{model_name}")
async def train_model(model_name:str,data: dict):
    target_adr = f"./back/model_data/{model_name}.json"
    response = Flow.predict(data,target_adr)
    return {"result": response[0],"rate":response[0]}

@app.get("/models")
def get_models():
    res = dict()
    res["models"] = Flow.model_list()
    return res

@app.get("/models/{model_name}")
def get_model_arc(model_name:str):
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)