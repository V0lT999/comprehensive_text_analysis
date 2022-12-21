import time

from kafka import KafkaProducer
from generate_text import generate_text

TOPIC = 'translation_topic'
TIME_SLEEP = 3


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)


def send_text():
    text = generate_text().encode('utf-8')
    producer.send(TOPIC, text)
    time.sleep(TIME_SLEEP)


if __name__ == '__main__':
    while True:
        send_text()
