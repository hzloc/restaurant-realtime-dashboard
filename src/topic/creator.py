from kafka import KafkaAdminClient
from kafka.admin.new_topic import NewTopic

kafka_configs = {
    "bootstrap_servers": ["localhost:29092"],
    "client_id": "admin_client"
}
admin_client = KafkaAdminClient(**kafka_configs)

if __name__ == "__main__":
    admin_client.create_topics(new_topics=[NewTopic(name="orders", num_partitions=3, replication_factor=3)])
