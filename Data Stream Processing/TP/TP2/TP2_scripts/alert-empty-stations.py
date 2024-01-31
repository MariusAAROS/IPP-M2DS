from kafka import KafkaConsumer
import json
from time import sleep

#-- constants
broker = "localhost:9092"
read_topic = "empty-stations"

#-- processses
consumer = KafkaConsumer(read_topic, bootstrap_servers=broker, group_id="app1")

for message in consumer:
    cur_data = json.loads(message.value.decode("utf-8"))
    for station in cur_data:
        if station["is_empty"] == 1:
            print(f"ALERT : Station {station['station']} is empty | city : {station['contract_name']} | address : {station['address']} ")
    sleep(1)