import paho.mqtt.client as mqtt
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)  # Adjust if necessary

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker:", rc)
    client.subscribe("relay")

def on_message(client, userdata, msg):
    message = msg.payload.decode().strip()
    print(f"Received MQTT message: {message}")

    if message == "ON":
        ser.write(b'1')
    elif message == "OFF":
        ser.write(b'0')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
