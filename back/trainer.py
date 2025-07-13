import pandas as pd
import json

from back.utils import Utils

class Trainer:

    def train(self,df,output_name):
        print("Starting training...")
        data = self.training(df)
        print("Training Complete.")
        Utils.export_json(output_name,data)
        print(f"Exported Training Data to {output_name}.")

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


    @staticmethod
    def _count_to_probability(data,count, smoothing=1):
        V = len(data)
        for key in data.keys():
            data[key] = (data[key]+ smoothing)/(count +smoothing * V )
        return data