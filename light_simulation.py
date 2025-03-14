import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "/student_group/light_control"

def on_message(client, userdata, message):
    payload = message.payload.decode()
    if payload == "ON":
        print("💡 Light is TURNED ON")
    elif payload == "OFF":
        print("💡 Light is TURNED OFF")

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

print("Listening for MQTT messages...")
client.loop_forever()
