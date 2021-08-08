import pika
import arrow
import os

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


def on_message(channel, method_frame, header_frame, body):
    print(f"received:  {arrow.utcnow()} - body: {body}")

    channel.basic_ack(
        delivery_tag = method_frame.delivery_tag
    )


connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.basic_consume('test', on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
