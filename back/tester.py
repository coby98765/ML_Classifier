import json
from back.predictor import Predictor


class Test:
    def __init__(self,model_rute):
        self.predictor = Predictor(model_rute)

    def run_test(self,df):
        test_df = df.iloc[:, :-1]
        result_df = df.iloc[:, -1:]
        rows = len(df)
        score = 0
        for i in range(rows):
            response = self.predictor.predict(test_df.iloc[i])

            actual_result = result_df.iloc[i].item()
            if response == actual_result:
                score +=1
        return (score/rows) * 100

    # @staticmethod
    # def import_json(file_name):
    #     file_rute = f".back//model_data/{file_name}_trained_data.json"
    #     with open(file_rute, 'r') as f:
    #         model = json.loads(f)
    #         return model