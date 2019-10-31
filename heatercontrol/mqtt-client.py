
# http://www.steves-internet-guide.com/into-mqtt-python-client/

from __future__ import print_function
import os
import paho.mqtt.client as mqtt
import time
import datetime
import relay as r

# must end with / if not empty
topic_root = "/balena/kalludden/"

def on_message(client, userdata, message):
    print("message received:", str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    # Note: message.retain will be 1 when this topic is received just after connecting
    # and the topic has been published as "retained".
    # message.retain is 0 when published while we are already connected.
    if str(message.payload.decode("utf-8")) == "ON":
        print("Turning relay on")
        r.close()
        client.publish(topic_root + "feedback/status", "ON", retain = True)
    else:
        print("Turning relay off")
        r.open()
        client.publish(topic_root + "feedback/status", "OFF", retain = True)
    client.publish(topic_root + "feedback/timestamp", str(datetime.datetime.utcnow()))

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        topic = topic_root + "control"
        print("Connected. Subscribing to topic", topic)
        client.subscribe(topic, qos=1)
        wait_for(client, "SUBACK")
    else:
        print("Error connecting. Code =", rc)

def on_disconnect(client, userdata, rc):
    print("Disconnect detected.  Code = ", rc)

def wait_for(client,msgType,period=0.25):
    if msgType=="SUBACK":
        if client.on_subscribe:
            while not client.suback_flag:
                print("waiting suback")
                client.loop()  #check for messages
                time.sleep(period)

my_id = os.environ.get("BALENA_DEVICE_UUID") or os.uname()[1]
broker_address = os.environ["MQTT_SERVER"]

print("creating new MQTT client instance with id", my_id)
client = mqtt.Client(my_id) #create new instance

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

print("connecting to broker", broker_address)
client.connect(broker_address) #connect to broker
client.loop_start() #handle mqtt loop in a separate thread

topic = topic_root + "startup"
print("Publishing message to topic", topic)
client.publish(topic, str(datetime.datetime.utcnow()), retain=True)

alive_period = 60
print("Starting main loop (sending alive message every {0} seconds)".format(alive_period))
topic = topic_root + "alive"
while True:
    time.sleep(alive_period)
    client.publish(topic, str(datetime.datetime.utcnow()))
