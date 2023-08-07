# consumer.py

import pika

def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    print(body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello_queue')

channel.basic_consume(queue='hello_queue',
                      on_message_callback=callback,
                      auto_ack=True)

channel.start_consuming()
