from kafka import KafkaConsumer, KafkaProducer
import json
from time import sleep

#-- constants
broker = "localhost:9092"
read_topic = "stations-status"
write_topic = "empty-stations"

#-- processses
consumer = KafkaConsumer(read_topic, bootstrap_servers=broker, group_id="app1")
producer = KafkaProducer(bootstrap_servers=broker, value_serializer=lambda v: json.dumps(v).encode("utf-8"))

empty = []
for message in consumer:
    to_send = []
    print("Received message | from topic : {}, partition: {}, offset: {}".format(
        message.topic, message.partition, message.offset)) 
    cur_data = json.loads(message.value.decode("utf-8"))
    for elem in cur_data:
        if elem["available_bikes"] == 0 and elem["number"] not in empty:
            to_send.append({"station": elem["number"], "contract_name":elem["contract_name"], "address":elem["address"], "is_empty":1})
            empty.append(elem["number"])
        elif elem["number"] in empty and elem["available_bikes"] != 0:
            to_send.append({"station": elem["number"], "is_empty":0})
            id = empty.index(elem["number"])
            empty.pop(id)
    if to_send != []:
        producer.send(write_topic, to_send)
        print(f"sent message to topic: {write_topic}")
    sleep(1)