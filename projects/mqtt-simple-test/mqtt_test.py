import paho.mqtt.client as mqtt
import platform

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))

print(platform.uname())

new_client=mqtt.Client()
new_client.on_connect
print(new_client)
local_port=1884
new_client.connect('0.0.0.0',local_port, 60)
