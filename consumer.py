from kafka import KafkaConsumer

TOPIC = 'translation_topic'

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='translator_group'
)


def get_text():
    for msg in consumer:
        print(msg.value.decode('utf'))


if __name__ == '__main__':
    get_text()
