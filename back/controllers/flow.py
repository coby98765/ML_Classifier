from back.utils.utils import Utils
from back.controllers.tester import Test
from back.models.trainer import Trainer
from back.models.classifier import Classifier

training = Trainer()

class Flow:
    @staticmethod
    def train_and_test(df, name):
        clean_df = Utils.clean_df(df)
        df_to_train, df_to_test = Utils.split_dataframe(clean_df)
        training.train(df_to_train, name)
        test = Test(name)
        accuracy = test.run_test(df_to_test)
        return accuracy

    @staticmethod
    def predict(data, name):
        target_adr = f"./back/model_data/{name}_trained_data.json"
        predictor = Classifier(target_adr)
        res =  predictor.predict(data)
        return res

    @staticmethod
    def model_list():
        folder = "./back/model_data"
        m_list = Utils.file_list(folder,'json')
        return m_list

    @staticmethod
    def model_arc(model_name):
        if model_name in Flow.model_list():
            model_data = Utils.import_json(f"./back/model_data/{model_name}.json")
            arc = Utils.module_arc(model_data)
            return arc
        else:
            return "model_not_found"
