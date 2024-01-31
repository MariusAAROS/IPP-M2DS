from kafka import KafkaConsumer, KafkaProducer
import json
from time import sleep

#-- constants
broker = "localhost:9092"
read_topic = "velib-stations"
write_topic = "stations-status"

#-- processses
consumer = KafkaConsumer(read_topic, bootstrap_servers=broker, group_id="app1")
producer = KafkaProducer(bootstrap_servers=broker, value_serializer=lambda v: json.dumps(v).encode("utf-8"))

prev_data = []
empty = True
for message in consumer:
    to_send = []
    print("Received message | from topic : {}, partition: {}, offset: {}".format(
        message.topic, message.partition, message.offset))
    cur_data = json.loads(message.value.decode("utf-8"))
    if empty:
        prev_data = cur_data[:]
        empty = False
    else:
        for elem, prev in zip(cur_data, prev_data):
            for attribute in elem.keys():
                if elem[attribute] != prev[attribute]:
                    to_send.append(elem)
                    break
        if to_send != []:
            producer.send(write_topic, to_send)
            print(f"sent message to topic: {write_topic}")
            prev_data = cur_data[:]

    sleep(1)