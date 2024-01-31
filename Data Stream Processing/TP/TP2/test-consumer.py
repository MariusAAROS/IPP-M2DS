import time
from kafka import KafkaConsumer

topic_name = "topic_name"
consumer = KafkaConsumer(topic_name, bootstrap_servers="localhost:9092", group_id="app1")
for message in consumer:
    print("Received message : {} from topic : {}, partition: {}, offset: {}".format(message.value,
    message.topic, message.partition, message.offset))
    time.sleep(1)