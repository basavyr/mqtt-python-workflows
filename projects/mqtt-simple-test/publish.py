import paho.mqtt.client as mqtt


client=mqtt.Client()


local='127.0.0.1'
host0='0.0.0.0'

client.connect(local, 1883,60)
client.connect(host0, 1883,60)



client.publish("test/","mmm")
