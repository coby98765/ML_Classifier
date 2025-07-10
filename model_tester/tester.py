import json
from predictor.predict import Predictor


class Test:
    def __init__(self,model_rute):
        self.predictor = Predictor(model_rute)

    def run_test(self,df):
        pass

    @staticmethod
    def import_json(self,file_rute):
        with open(file_rute, 'r') as f:
            model = json.loads(f)
            return model