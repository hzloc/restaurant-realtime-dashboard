from kafka.producer import KafkaProducer
from src.faker.order import order_schema
from src.serializer.json_serializer import JSONSerializer

if __name__ == "__main__":
    kafka_configs = {
        "bootstrap_servers": ["localhost:29092", "localhost:39092", "localhost:49092"],
        "client_id": "kafka-client-producer-orders",
        "value_serializer": lambda m: JSONSerializer.serialize(m)
    }
    order_producer = KafkaProducer(**kafka_configs)
    if order_producer.bootstrap_connected():
        print("Bootstrap connected! Server is working.")

    # create orders non-stop
    while True:
        order_schema.create()
        for order in order_schema:
            order_producer.send(topic="orders", value=order)