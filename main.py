import requests
import json
import datetime
from datetime import timedelta


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").text

data = json.loads(response)

print(data)

print('----------------------------')

date_time = datetime.datetime.strptime(data['time']['updated'], '%b %d, %Y %H:%M:%S %Z')

# date_formatted = datetime.datetime.strftime(data_time, '%Y.%m.%d')
# time_formatted = datetime.datetime.strptime(data_time, '%H:%M:%S').time()
date_time = date_time + timedelta(hours=5) #Время Астаны
print(type(date_time))
count_on_dollars = data['bpi']['USD']['rate_float']

print(date_time, count_on_dollars)



