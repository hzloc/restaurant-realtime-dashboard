from kafka.consumer import KafkaConsumer
from src.serializer.json_serializer import JSONSerializer
from src.db import insert_into_db

order_consumer = KafkaConsumer('orders',
                               group_id="order-groups",
                               bootstrap_servers= ["localhost:29092", "localhost:39092", "localhost:49092"],
                               value_deserializer=lambda m: JSONSerializer.deserialize(m)
                               )
if __name__ == "__main__":
    for message in order_consumer:
        insert_into_db(message.value, "orders")