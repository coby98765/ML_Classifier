from predictor.predict import Predictor
from trainer.train_model import Trainer

project = "phishing"
data_csv = f"./data/{project}.csv"

# training = Trainer()
# training.train(data_csv,project)

predictor = Predictor(project)
predictor.load_model()

sample_input = {
    "UsingIP": 1,
    "LongURL": -1,
    "ShortURL": 1,
    "Symbol@": 1,
    "Redirecting//": 1,
    "PrefixSuffix-": -1,
    "SubDomains": 0,
    "HTTPS": -1,
    "DomainRegLen": -1,
    "Favicon": 1,
    "NonStdPort": 1,
    "HTTPSDomainURL": 1,
    "RequestURL": -1,
    "AnchorURL": 0,
    "LinksInScriptTags": -1,
    "ServerFormHandler": -1,
    "InfoEmail": 1,
    "AbnormalURL": 1,
    "WebsiteForwarding": 0,
    "StatusBarCust": 1,
    "DisableRightClick": 1,
    "UsingPopupWindow": 1,
    "IframeRedirection": 1,
    "AgeofDomain": -1,
    "DNSRecording": 1,
    "WebsiteTraffic": 0,
    "PageRank": -1,
    "GoogleIndex": 1,
    "LinksPointingToPage": 0,
    "StatsReport": 1
}
print(predictor.predict(sample_input))