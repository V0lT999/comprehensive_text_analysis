from kafka import KafkaConsumer
from translator import translate
from translation_producer import send_translation

TOPIC = 'translation_topic'

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='translator_group'
)


def get_text():
    for msg in consumer:
        text = msg.value.decode('utf-8')
        translation = translate(text)
        send_translation(text=text, translation=translation)
        print(f'sent text: {text}')


if __name__ == '__main__':
    get_text()
