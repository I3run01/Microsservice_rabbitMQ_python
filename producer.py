# producer.py

import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (creates if not exists)
channel.queue_declare(queue='hello_queue')

# Send a message
channel.basic_publish(exchange='',
                      routing_key='hello_queue',
                      body='hello')

print("Sent 'hello'")

connection.close()
