import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garantir que a fila 'hello' exista
channel.queue_declare(queue='hello')

# Consumir da fila
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
