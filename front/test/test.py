import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError

url = r"http://127.0.0.1:8000/"

r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.json())
else:
    print(f"Error, code: {r.status_code}, ")

item = input("Enter item id: ")

try:
    response = requests.get(f'{url}items/{item}')
    response.raise_for_status() # Raise HTTPError for bad status codes
except Exception as e:
    print(f"An error occurred: {e}")