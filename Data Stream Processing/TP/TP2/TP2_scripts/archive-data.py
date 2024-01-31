from kafka import KafkaConsumer
import json
from time import sleep

#--prerequisite
#type the following command in the prompt
#./bin/kafka-topics.sh --create --topic velib-stations --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092

#-- constants
broker = "localhost:9092"
read_topic = "velib-stations"

#-- processes
consumer = KafkaConsumer(read_topic, bootstrap_servers=broker, group_id="app1")

for message in consumer:
    to_send = []
    cur_data = str(message.value)
    with open("archive.json", "w") as outfile:
        outfile.write(cur_data)
    print("Archived")