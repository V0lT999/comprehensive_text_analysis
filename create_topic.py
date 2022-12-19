from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id='test'
)


def create_topic():
    topic_list = list()
    topic_list.append(NewTopic(name="translation_topic", num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)


if __name__ == "__main__":
    create_topic()
