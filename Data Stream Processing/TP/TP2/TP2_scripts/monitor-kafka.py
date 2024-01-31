import time
from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers = 'localhost:9092', group_id='monitor')
consumer.subscribe(['velib-stations', 'empty-stations', 'stations-status'])

for message in consumer:
    print(f'Topic: {message.topic}, Partition: {message.partition}, Offset: {message.offset}, Timestamp: {message.timestamp}')



    