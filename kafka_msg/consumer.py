from ensurepip import bootstrap
import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        "orders",
        bootstrap_servers = "localhost:9092",
        value_deserializer = lambda m: json.loads(m.decode('ascii'))
    )
    for message in consumer:
        print("message received:")
        print(str(message.value))
    
