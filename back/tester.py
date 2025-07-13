import json
from back.predictor import Predictor
from back.utils import Utils


class Test:
    def __init__(self,model_rute):
        self.name = model_rute
        self.predictor = Predictor(model_rute)
        self.score = 0

    def run_test(self,df):
        # split df
        test_df = df.iloc[:, :-1]
        result_df = df.iloc[:, -1:]
        rows = len(df)
        score = 0
        for i in range(rows):
            response = self.predictor.predict(test_df.iloc[i])
            actual_result = result_df.iloc[i].item()
            # print("actual_result: ",actual_result,"response: ",response)
            if response[0] == str(actual_result):
                score +=1

        # calculate percent
        if rows > 0:
            self.score = (score / rows) * 100
        #add score in model data
        self.add_score_to_json()
        return self.score

    def add_score_to_json(self):
        data = Utils.import_json(self.name)
        data['accuracy'] = self.score
        Utils.export_json(self.name,data)
