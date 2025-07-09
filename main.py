# from predictor.predict import
from trainer.train_model import Trainer

data_csv = r"./data/phishing.csv"

training = Trainer()
training.train(data_csv,"phishing")