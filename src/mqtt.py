from umqtt.simple import MQTTClient
import ubinascii
import machine
import control

# Default MQTT server to connect to
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
SERVER = "192.168.0.15"
PORT = 1883
USER = None
PASSWORD = None

TOPIC = b"4gcar"


def sub_cb(topic, msg):
    control.detail(topic, msg)


def subscribe():
    c = MQTTClient(client_id=CLIENT_ID, server=SERVER, port=PORT, user=USER, password=PASSWORD)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (SERVER, TOPIC))

    try:
        while True:
            c.check_msg()
    finally:
        c.disconnect()
