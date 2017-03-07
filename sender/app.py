from sensors import PIR
import paho.mqtt.client as mqtt

def PIR_triggered(name):
    print (name, "fired sensor")
    client.publish(ch, "1")
    print ("-")

pir1 = PIR(17, "PIR1", PIR_triggered)

ch = "6aff59edc87ea1b5db2ec47f807ef1267fa698a7"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
#client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()

