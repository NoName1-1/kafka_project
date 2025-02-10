from kafka import KafkaProducer
import requests
import json
import datetime
from datetime import timedelta
import time

from pyexpat.errors import messages

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

while True:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").text

    data = json.loads(response)

    print(data)

    print('----------------------------')

    date_time = datetime.datetime.strptime(data['time']['updated'], '%b %d, %Y %H:%M:%S %Z')

    # date_formatted = datetime.datetime.strftime(data_time, '%Y.%m.%d')
    # time_formatted = datetime.datetime.strptime(data_time, '%H:%M:%S').time()
    date_time = date_time + timedelta(hours=5) #Время Астаны
    date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
    print(type(date_time))
    count_on_dollars = data['bpi']['USD']['rate_float']

    print(date_time, count_on_dollars)
    message = {'timestamp': date_time, 'price': count_on_dollars}

    producer.send(topic='bitcoin_value', value=message)
    print(f"{message} sent")
    time.sleep(3600)



