import requests
url = 'https://test3.diavgeia.gov.gr/luminapi/opendata/decisions/%CE%92%CE%A73%CE%9A%CE%A1%CE%A92-%CE%A6%CE%9D%CE%9B.json'
response = requests.get(url)
#print(response.json())

import json

data = json.loads(response.text)

print("Απόφαση: " + data['subject'])


