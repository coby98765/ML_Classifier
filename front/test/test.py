import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError

url = r"http://127.0.0.1:8000/"

r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.json())
else:
    print(f"Error, code: {r.status_code}, ")

try:
    response = requests.get(f'{url}models')
    response.raise_for_status() # Raise HTTPError for bad status codes
except Exception as e:
    print(f"An error occurred: {e}")


list_res = response.json()
print(list_res)
item = list_res['models'][0]
print(item)

try:
    response = requests.get(f'{url}models/{item}')
    response.raise_for_status() # Raise HTTPError for bad status codes
    print(response.json())
except Exception as e:
    print(f"An error occurred: {e}")

# item_res = response.json()
# print(item_res)
