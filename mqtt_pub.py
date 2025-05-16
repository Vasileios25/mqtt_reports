import sys
import paho.mqtt.client as paho
import ssl
import time
import random

BROKER = "mqtt.sparkworks.cloud"
PORT = 8883
USERNAME = "admin"
PASSWORD = "public"
<<<<<<< HEAD
<<<<<<< HEAD
MESSAGE = "hola como estas"
=======
MESSAGE = "hello world"
>>>>>>> 5a9bb8a (fix some issues with topic, throws errors with cliend id so remove it for now)
=======

MESSAGE = "hola como estas"

>>>>>>> c3f31b6 (Initial push with secure Slack token handling)
CLIENT_ID = f'python-mqtt-{random.randint(0, 800)}'
TOPIC = "test"


# Callback function when connection is established and publish to the topic
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected with result code {rc}")
        #client.publish("test", "Hi, paho mqtt client works fine!", 0)
    else:
        print(f" Connection failed with result code{rc}")


def connect_mqtt():
    client = paho.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLS)
    client.tls_insecure_set(True)
    client.on_connect = on_connect #Set callbacks

    if client.connect(BROKER, PORT, 60) != 0:
        print("Couldn't connect to the MQTT broker")
        sys.exit(1)

    return client



def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
<<<<<<< HEAD
<<<<<<< HEAD
        msg = f"message {MESSAGE}: {msg_count}"
=======
        msg = f"messages: {msg_count}"
>>>>>>> 5a9bb8a (fix some issues with topic, throws errors with cliend id so remove it for now)
=======
        msg = f"messages: {msg_count}"
=======
        msg = f"message {MESSAGE}: {msg_count}"
>>>>>>> 0ab77c0 (Initial push with secure Slack token handling)
>>>>>>> c3f31b6 (Initial push with secure Slack token handling)
        result = client.publish(TOPIC, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{TOPIC}`")
        else:
            print(f"Failed to send message to topic {TOPIC}")
        msg_count += 1
        if msg_count > 2:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()
    client.disconnect()
    print("Disconnected from MQTT broker")


if __name__ == '__main__':
    run()

# Start the loop to handle messages and connection
#client.loop_start()

# Let the connection live briefly to allow publish
#time.sleep(15)

# Disconnect
#client.loop_stop()
#client.disconnect()
