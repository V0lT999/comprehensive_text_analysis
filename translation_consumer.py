from kafka import KafkaConsumer

TOPIC = 'result_topic'

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='result_group'
)


def get_text():
    for msg in consumer:
        print(msg.value.decode('utf-8'))


if __name__ == '__main__':
    get_text()
