import os
import datetime
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('neo4j',
    # bootstrap_servers=['localhost:9092','localhost:29092'],
    bootstrap_servers=['localhost:9092'],
    sasl_mechanism="PLAIN",
    # security_protocol="PLAINTEXT", 
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: x.decode("utf-8"))

print(datetime.datetime.now(), "Started Kafka Consumer")
for msg in consumer:
    print("\n\n Processing msg")
    message_dict = json.loads(msg.value)

    print(datetime.datetime.now())
    print("%s" % (json.dumps(message_dict,indent=4)))