import sys
import paho.mqtt.client as paho
<<<<<<< HEAD
<<<<<<< HEAD
import ssl
import time
import random
import json  # Importing json module
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> c3f31b6 (Initial push with secure Slack token handling)
import argparse
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
load_dotenv()
<<<<<<< HEAD
=======
import ssl
import time
import random
>>>>>>> 6c45725 (add function, connection with creds and more)
=======
>>>>>>> b12a60e (client.subscribe(TOPIC) moved inside on_connect(), so the subscription happens after a successful connection,on_message() callback added for receiving and printing messages when they arrive.)
=======
>>>>>>> 0ab77c0 (Initial push with secure Slack token handling)
>>>>>>> c3f31b6 (Initial push with secure Slack token handling)

BROKER = "mqtt.sparkworks.cloud"
PORT = 8883
USERNAME = "admin"
PASSWORD = "public"
<<<<<<< HEAD
<<<<<<< HEAD
MESSAGE = "hola como estas"
TOPIC = "test"

TOKEN = os.getenv("SLACK_API_TOKEN")
CHANNEL = 'C08QHB55CNT'
# Generate a Client ID with the subscribe prefix.
CLIENT_ID = f'subscribe-{random.randint(0, 100)}'


# Callback function when connection is established and subscribe to the topic
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected with result code {rc}")
        client.subscribe(TOPIC)  # Subscribe to the topic here
        print(f"Subscribed to topic: {TOPIC}")
    else:
        print(f"Connection failed with result code {rc}")




# Callback function when a message is received
def on_message(client, userdata, msg):
    try:
        message_text = msg.payload.decode()  # Decode the byte payload to a string
        print(f"Received `{message_text}` from `{msg.topic}` topic")
        
        slack_client = WebClient(token=TOKEN)
        slack_client.chat_postMessage(
            channel=CHANNEL,
            text=f"MQTT message received on `{msg.topic}`: {message_text}"
        )
    except SlackApiError as e:
        print(f"Slack API Error: {e.response['error']}")
    except Exception as e:
        print(f"Caught an Exception: {e}")

# Send a message


def connect_mqtt():
    client = paho.Client()  # MQTT client initialization to establish connection to broker
    client.username_pw_set(USERNAME, PASSWORD)  # Authentication to broker with username and password
    client.tls_set(cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLS)  # Configure TLS/SSL with no certificate verification for self-signed certificates
    client.tls_insecure_set(True)  # Skip hostname verification for testing
    client.on_connect = on_connect  # Set on_connect callback
    client.on_message = on_message  # Set on_message callback

    if client.connect(BROKER, PORT, 60) != 0:
        print("Couldn't connect to the MQTT broker")
        sys.exit(1)

    return client


# Start the loop to listen for incoming messages
def run():
    client = connect_mqtt()
    try:
        print("Press CTRL+C to exit...")
        client.loop_forever()
    except Exception as e:
        print(f"Caught an Exception: {e}")
    finally:
        print("Disconnecting from the MQTT broker")
        client.disconnect()








if __name__ == '__main__':
    run()
    
=======
=======
=======
>>>>>>> c3f31b6 (Initial push with secure Slack token handling)
MESSAGE = "hello world"
TOPIC = "test"
=======
MESSAGE = "hola como estas"
TOPIC = "test"

TOKEN = os.getenv("SLACK_API_TOKEN")
CHANNEL = 'C08QHB55CNT'
>>>>>>> 0ab77c0 (Initial push with secure Slack token handling)
# Generate a Client ID with the subscribe prefix.
CLIENT_ID = f'subscribe-{random.randint(0, 100)}'
>>>>>>> 6c45725 (add function, connection with creds and more)


# Callback function when connection is established and subscribe to the topic
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected with result code {rc}")
        client.subscribe(TOPIC)  # Subscribe to the topic here
        print(f"Subscribed to topic: {TOPIC}")
    else:
        print(f"Connection failed with result code {rc}")

<<<<<<< HEAD
# Callback function when a message is received
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())  # Assuming payload is JSON
    print(f"Received `{payload}` from `{msg.topic}` topic")
=======



# Callback function when a message is received
def on_message(client, userdata, msg):
    try:
        message_text = msg.payload.decode()  # Decode the byte payload to a string
        print(f"Received `{message_text}` from `{msg.topic}` topic")
        
        slack_client = WebClient(token=TOKEN)
        slack_client.chat_postMessage(
            channel=CHANNEL,
            text=f"MQTT message received on `{msg.topic}`: {message_text}"
        )
    except SlackApiError as e:
        print(f"Slack API Error: {e.response['error']}")
    except Exception as e:
        print(f"Caught an Exception: {e}")

# Send a message
>>>>>>> 0ab77c0 (Initial push with secure Slack token handling)


def connect_mqtt():
    client = paho.Client()  # MQTT client initialization to establish connection to broker
    client.username_pw_set(USERNAME, PASSWORD)  # Authentication to broker with username and password
    client.tls_set(cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLS)  # Configure TLS/SSL with no certificate verification for self-signed certificates
    client.tls_insecure_set(True)  # Skip hostname verification for testing
    client.on_connect = on_connect  # Set on_connect callback
    client.on_message = on_message  # Set on_message callback

    if client.connect(BROKER, PORT, 60) != 0:
        print("Couldn't connect to the MQTT broker")
        sys.exit(1)

    return client


# Start the loop to listen for incoming messages
def run():
    client = connect_mqtt()
    try:
        print("Press CTRL+C to exit...")
        client.loop_forever()
    except Exception as e:
        print(f"Caught an Exception: {e}")
    finally:
        print("Disconnecting from the MQTT broker")
        client.disconnect()


<<<<<<< HEAD
if __name__ == '__main__':
    run()



<<<<<<< HEAD
<<<<<<< HEAD
try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except Exception as e:
    print(f"Caught an Exception: {e}")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()
>>>>>>> a3ef1b8 (Initial commit with setup files)
=======
>>>>>>> 6c45725 (add function, connection with creds and more)
=======
=======






if __name__ == '__main__':
    run()
    
>>>>>>> 0ab77c0 (Initial push with secure Slack token handling)
>>>>>>> c3f31b6 (Initial push with secure Slack token handling)
