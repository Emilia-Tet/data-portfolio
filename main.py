import pandas as pd
import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A/last/30/?format=json"

response = requests.get(url)
data = response.json()

rows = []
for entry in data:
    date = entry['effectiveDate']
    for rate in entry['rates']:
        rows.append({
            'date': date,
            'currency': rate['currency'],
            'code': rate['code'],
            'mid': rate['mid']
        })

df = pd.DataFrame(rows)
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)
print(df.head())
