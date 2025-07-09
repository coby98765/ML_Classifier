# from predictor.predict import
from trainer.train_model import Trainer

data_csv = r"./data/phishing.csv"

training = Trainer(data_csv,output_name="phishing")
training.train()