import paho.mqtt.client as mqtt
import platform
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

print(platform.uname())

new_client=mqtt.Client()
new_client.on_connect=on_connect
new_client.on_message=on_message

host='0.0.0.0'
host_1='127.0.0.1'
local_port1=1883
local_port2=1884
local_port3=1885

new_client.connect(host,local_port1, 60)
#new_client.connect(host,local_port2, 60)
#new_client.connect(host,local_port3, 60)

#for i in range(10):
#	new_client.publish("test/",'hey for v0')
#	new_client.publish("test/v2",'hey for v2')
#	time.sleep(1)

new_client.subscribe("test/")

new_client.loop_forever()
