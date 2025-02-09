import requests
import json


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").text

data = json.loads(response)

print(data)

print('----------------------------')

print(data['time']['updated'], data['bpi']['USD']['rate_float'])



