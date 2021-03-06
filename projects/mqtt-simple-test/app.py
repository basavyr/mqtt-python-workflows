import os
import time
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


host_ip = '172.17.0.2'
port = 1883 
host0='0.0.0.0'
keepalive = 60
topic = 'test/'


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('127.0.0.1', port, keepalive)
client.subscribe(topic)
client.publish(topic,"mmm")
client.loop_forever()
