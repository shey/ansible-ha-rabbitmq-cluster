import pika
import time
import os
import arrow

credentials = pika.PlainCredentials(
    os.getenv("RABBITMQ_USERNAME", "bugs"),
    os.getenv("RABBITMQ_PASSWORD", "bunny")
)

connection_params = pika.ConnectionParameters(
    '192.168.114.101',
    5672,
    "/",
    credentials
)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='test', durable=True)

for count, value in enumerate(range(2,300)):
    body = f"Hello {count} - time_registered {arrow.utcnow()}"

    print(body)

    channel.basic_publish(
        exchange='',
        routing_key='test',
        body=body
    )

    time.sleep(1)

connection.close()
