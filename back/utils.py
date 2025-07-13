import pandas as pd
import json

class Utils:
    @staticmethod
    def split_dataframe(df, train_ratio=0.7):
        shuffled = df.sample(frac=1,random_state=5)
        split_index = int(len(shuffled) * train_ratio)
        train_df = shuffled.iloc[:split_index]
        test_df = shuffled.iloc[split_index:]
        return train_df, test_df

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
    def clean_df(df):
        print("Cleaning Data...")
        clean_df = df.copy()
        for col in clean_df.columns:
            unique_vals = clean_df[col].nunique()
            total_vals = len(clean_df[col])
            if unique_vals == total_vals or unique_vals == 1:
                print(f"Dropping Column: {col}.")
                clean_df.drop(columns=col, inplace=True)
        return clean_df

    @staticmethod
    def import_json(file_rute):
        with open(file_rute, 'r') as f:
            model = json.load(f)
            return model

    @staticmethod
    def export_json(file_rute,data):
        #adjusting data keys to match JSON prot.
        clean_model = Utils._convert_keys_to_str(data)
        with open(file_rute, 'w') as f:
            json.dump(clean_model, f, indent=2)

    @staticmethod
    def _convert_keys_to_str(obj):
        if isinstance(obj, dict):
            return {str(k): Utils._convert_keys_to_str(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [Utils._convert_keys_to_str(i) for i in obj]
        else:
            return obj