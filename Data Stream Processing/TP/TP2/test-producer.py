import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092", value_serializer=str.encode)
i = 0
topic_name = "topic1"
while True:
    message = "message-{}".format(i)
    producer.send(topic_name, message)
    print("Sending message {} to topic: {}".format(message, topic_name))
    i += 1
    time.sleep(1)