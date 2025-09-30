import pika

# Conectar ao RabbitMQ (localhost por padrão)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garantir que a fila 'hello' exista
channel.queue_declare(queue='hello')

# Publicar mensagem
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()
