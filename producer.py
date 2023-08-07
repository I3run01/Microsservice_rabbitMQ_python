import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue = channel.queue_declare(queue='hello_queue')

# Send a message
channel.basic_publish(exchange='',
                      routing_key=queue,
                      body='hello')

print("Sent 'hello'")

connection.close()
