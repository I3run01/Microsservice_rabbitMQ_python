# consumer.py

import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    if body.decode() == 'hello':
        print(" [x] Hello, World")

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue as in producer to make sure it exists
channel.queue_declare(queue='hello_queue')

# Set up a consumer on the queue
channel.basic_consume(queue='hello_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
