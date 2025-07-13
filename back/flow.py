from back.utils import Utils
from back.tester import Test
from back.trainer import Trainer
from back.predictor import Predictor


training = Trainer()

class Flow:
    @staticmethod
    def train_and_test(df, name):
        test = Test(name)
        clean_df = Utils.clean_df(df)
        df_to_train, df_to_test = Utils.split_dataframe(clean_df)
        training.train(df_to_train, name)
        accuracy = test.run_test(df_to_test)
        return accuracy

    @staticmethod
    def predict(data, name):
        target_adr = f"./back/model_data/{name}_trained_data.json"
        predictor = Predictor(target_adr)
        predictor.predict(data)
        return accuracy