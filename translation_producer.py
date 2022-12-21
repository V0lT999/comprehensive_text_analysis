from kafka import KafkaProducer

TOPIC = 'result_topic'

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)


def send_translation(text: str, translation: str):
    result_text = f'text: {text}\ntranslation: {translation}'.encode('utf-8')
    producer.send(TOPIC, result_text)
    print(f'put text: {result_text}')


if __name__ == '__main__':
    send_translation('Перевод', 'Translation')
