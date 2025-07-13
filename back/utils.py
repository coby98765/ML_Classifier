import pandas as pd

from back.trainer import Trainer
from back.tester import Test

training = Trainer()
test = Test()


class Utils:
    @staticmethod
    def split_dataframe(df, train_ratio=0.7):
        shuffled = df.sample(frac=1)
        split_index = int(len(shuffled) * train_ratio)
        train_df = shuffled.iloc[:split_index]
        test_df = shuffled.iloc[split_index:]
        return train_df, test_df

    @staticmethod
    def train_and_test(df,name):
        clean_df = Utils._clean_df(df)
        df_to_train, df_to_test = Utils.split_dataframe(clean_df)
        training.train(df_to_train,name)
        test.run_test(df_to_test,name)

        pass

    @staticmethod
    def get_df(input_file):
        try:
            df = pd.read_csv(input_file)
            print("CSV file loaded successfully!")
            print(df.info())
            return df
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    #clean DF from unique col (like index,id)
    # or if one value for all lines in col
    @staticmethod
    def _clean_df(df):
        clean_df = df.copy()
        for col in clean_df.columns:
            unique_vals = clean_df[col].nunique()
            total_vals = len(clean_df[col])
            if unique_vals == total_vals or unique_vals == 1:
                print(f"Dropping Column: {col}.")
                clean_df.drop(columns=col, inplace=True)
        return clean_df