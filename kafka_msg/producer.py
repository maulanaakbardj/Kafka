from ensurepip import bootstrap
import json
from kafka import KafkaProducer

if __name__ == '__main__':
    print("Starting Kafka Producer..")
    producer = KafkaProducer(
        bootstrap_servers = "localhost:9092",
        value_serializer = lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send("orders", "order3")
    producer.flush()
    print("message produced")
