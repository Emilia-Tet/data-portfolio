import pandas as pd
import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A/last/30/?format=json"

response = requests.get(url)
data = response.json()

print(data)