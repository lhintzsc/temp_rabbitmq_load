#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='myQueue')


def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    pass


channel.basic_consume(
    queue='myQueue', on_message_callback=callback, auto_ack=True)

#print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
