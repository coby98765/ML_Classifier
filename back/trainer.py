import pandas as pd
import json

class Trainer:
    def __init__(self):
        self.csv_file = ""
        self.json_file = ""
        self.df = None
        self.data = None

    def train(self,df,output_name=""):
        # self.csv_file = input_file
        self.json_file = f"./model_data/{output_name}_trained_data.json"
        # print("Getting data.")
        # df = self.get_df(self.csv_file)
        # print("Data info: ")
        # print(df.info())
        print("Cleaning Data...")
        self.df = self._clean_df(df)
        print("Starting training...")
        self.data = self.training(self.df)
        print("Training Complete.")
        self.save()
        print(f"Exported Training Data to {self.json_file}.")

    def training(self,df,data=None):
        if data is None:
            data = dict()
        data["columns"] = df.columns.tolist()
        label_col = data["columns"][-1]
        data["sum"] = df[label_col].value_counts().to_dict()
        data["data"] = dict()
        final_ops = df[label_col].unique().tolist()
        for option in final_ops:
            data["data"][option] = dict()
            for key in data["columns"]:
                if key == label_col:
                    continue
                amount_dict = df[df[label_col] == option][key].value_counts().to_dict()
                for val in df[key].unique():
                    amount_dict.setdefault(val, 0)
                data["data"][option][key] = self._count_to_probability(amount_dict,data["sum"][option])
        return data

    def save(self):
        #adjusting data keys to match JSON prot.
        clean_model = self._convert_keys_to_str(self.data)
        with open(self.json_file, 'w') as f:
            json.dump(clean_model, f, indent=2)

    #utils
    #gpt solution for dict keys not compatible for JSON
    def _convert_keys_to_str(self,obj):
        if isinstance(obj, dict):
            return {str(k): self._convert_keys_to_str(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_keys_to_str(i) for i in obj]
        else:
            return obj

    @staticmethod
    def _count_to_probability(data,count, smoothing=1):
        V = len(data)
        for key in data.keys():
            data[key] = (data[key]+ smoothing)/(count +smoothing * V )
        return data