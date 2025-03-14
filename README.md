# MQTT Light Control

This project demonstrates a simple IoT light control system using MQTT.

## Features
- A web-based UI to send ON/OFF commands.
- A simulated IoT device (ESP8266) using Python.
- Real-time MQTT communication over WebSockets.

## How to Run
1. Install dependencies: `pip install paho-mqtt`
2. Start the MQTT subscriber: `python light_simulation.py`
3. Open `index.html` in a browser.
4. Click the buttons to turn the light ON/OFF.

## Technologies Used
- HTML, JavaScript (MQTT.js)
- Python (paho-mqtt)
- Mosquitto MQTT Broker


