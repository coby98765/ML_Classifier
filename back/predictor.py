import json

from back.utils import Utils

class Predictor:
    def __init__(self,data_file_name):
        self.file_adr = data_file_name
        self.data = Utils.import_json(self.file_adr)


    def predict(self,entry):
        cal = self._create_cal_dict(entry)
        final_options = self._sum_key(cal)
        normalized_vals = self._normalize_and_scale(final_options)
        max_option = max(normalized_vals, key=normalized_vals.get)
        return max_option,normalized_vals

    def load_model(self):
        with open(self.file_adr, 'r') as f:
            self.data = json.load(f)
        # print(self.data)

    #utils
    #create a dict or the options based on model
    def _create_cal_dict(self,entry):
        if set(entry.keys()) != set(self.data["columns"][:-1]):
            print("Data dos not match model.")
            return None
        cal = dict()
        options = self.data["sum"].keys()
        for option in options:
            cal[option] = dict()
            for col in entry.keys():
                x = entry[col]
                cal[option][col] = self.data["data"][option][col][str(x)]
        return cal

    #calculate options rate
    @staticmethod
    def _sum_key(options_data):
        final_options = dict()
        for key in options_data.keys():
            key_sum = 1
            for col in options_data[key].keys():
                key_sum *= options_data[key][col]
            final_options[key] = key_sum
        return final_options
    
    @staticmethod
    def _normalize_options(dict_in):
        value_map = {
            1: "yes",
            -1: "no",
            0: "none",
            "1": "yes",
            "-1": "no",
            "0": "none"
        }
        return {
            value_map.get(key, key) :value
            for key, value in dict_in.items()
        }

    @staticmethod
    def _normalize_and_scale(scores, epsilon=1e-9):
        # Add small epsilon to avoid zeros
        scores = {k: v + epsilon for k, v in scores.items()}

        # Normalize to get probabilities that sum to 1
        total = sum(scores.values())
        normalized = {k: v / total for k, v in scores.items()}

        # Optional: Rescale to percentages
        scaled = {k: round(v * 100, 2) for k, v in normalized.items()}

        return scaled
