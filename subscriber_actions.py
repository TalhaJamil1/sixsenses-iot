import ssl
import paho.mqtt.client as mqtt

#inbox = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("commandandcontrol/#")

def on_message(client, user_data, msg):
    #inbox.append(str(msg.payload.decode("utf-8")))
    print(msg.topic)
    if msg.topic == "commandandcontrol/ms" and str(msg.payload.decode("utf-8")) == "1":
        print("Capturing Picture!!!")
    
    print(str(msg.payload.decode("utf-8")) )
    

client = mqtt.Client(client_id='RPi-000000002017')
client.username_pw_set(username="commandandcontrol", password="Qpc423hwdM")
client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect("cwlicc.zapto.org", 8883, 60)
#client.subscribe("script")

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()