RabbitMQ Hello World em Python

Este projeto é um exemplo simples de **produtor e consumidor** usando o [RabbitMQ](https://www.rabbitmq.com/) com Python e a biblioteca [pika](https://pika.readthedocs.io/).  
É o clássico "Hello World!" do RabbitMQ.

Pré-requisitos

- [Python 3](https://www.python.org/downloads/)
- [RabbitMQ](https://www.rabbitmq.com/download.html) instalado e em execução  
(por padrão ele roda em `localhost:5672`)
- Biblioteca **pika**:
  ```bash
  pip install pika
Executando o código
1.Inicia-se o RabbitMQ:
código: rabbitmq-server

2.Em um terminal, rode o consumidor:
código:python receiver.py
saída esperada:
[*] Waiting for messages. To exit press CTRL+C

3.Em outro terminal, rode o produtor:
código: python sender.py
saída do produtor:
 [x] Sent 'Hello World!'
saída do consumidor:
 [x] Received Hello World!

Referências

RabbitMQ - Getting Started
pika - Python client


