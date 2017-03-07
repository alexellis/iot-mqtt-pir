import paho.mqtt.client as mqtt

ch = "6aff59edc87ea1b5db2ec47f807ef1267fa698a7"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(ch)

def on_message(client, userdata, msg):
#    if msg.topic == ch:
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
