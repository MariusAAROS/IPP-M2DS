import time
import json
import requests
from kafka import KafkaProducer

#-- constants
key = "d9f535e356ac681337c7f8a959564848477ae711"
api_url = f"https://api.jcdecaux.com/vls/v1/stations?apiKey={key}"
broker = "localhost:9092"
topic = "velib-stations"


#-- utils
def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from the API: {e}")
        return None


#-- processes
producer = KafkaProducer(bootstrap_servers=broker,
                        value_serializer=lambda v: json.dumps(v).encode("utf-8"))

while True:
    data = fetch_data(api_url)
    try:
        producer.send(topic, value=data)
        print("Sent message to topic: {}".format(topic))
    except Exception as e:
        print(f"Failed to push message to Kafka: {e}")
    time.sleep(10)