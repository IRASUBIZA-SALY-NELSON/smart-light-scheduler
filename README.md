
# Smart Light Scheduler

**Smart Light Scheduler** is an IoT-based project designed to schedule and control lights using MQTT and WebSocket protocols. It allows users to set ON and OFF times for lights through a web-based interface, and the system communicates with an Arduino board to control a relay that turns the light on or off based on the schedule.

This project leverages a combination of **frontend technologies**, **WebSocket communication**, **MQTT messaging**, and **Arduino** programming to create an efficient and interactive light scheduling system.

## Key Features

- **Web Interface**: User-friendly interface to set ON and OFF times for the light.
- **WebSocket Communication**: Seamless communication between the frontend and backend via WebSocket.
- **MQTT Protocol**: Reliable and efficient messaging system for controlling the light via MQTT.
- **Arduino Integration**: Sends signals to an Arduino board to control the relay and turn the light on or off based on the schedule.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, WebSocket
- **MQTT**: Mosquitto Broker
- **Arduino**: C++ programming for Arduino Uno
- **Libraries & Tools**:
  - `paho.mqtt.client` (Python)
  - `websockets` (Python)
  - `mosquitto_pub` & `mosquitto_sub`
  - Arduino IDE

## Project Structure

```
/smart-light-scheduler
│
├── /frontend
│   ├── index.html           # Main HTML file
│   ├── styles.css           # CSS styles for the UI
│   ├── script.js            # JavaScript for WebSocket and form handling
│
├── /backend
│   ├── server.py            # Python WebSocket server for receiving schedules
│   ├── mqtt_subscriber.py   # Python script for subscribing to MQTT messages and controlling the light
│
├── /arduino
│   ├── light_control.ino    # Arduino code for controlling the relay based on serial input
│
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Installation

### Prerequisites

1. **Arduino IDE**: Install the Arduino IDE to upload code to the Arduino board.
2. **Python 3.x**: Make sure Python 3.x is installed. You can download it from [here](https://www.python.org/downloads/).
3. **MQTT Broker**: Install [Mosquitto](https://mosquitto.org/), which will act as the MQTT broker for message exchange.

### Backend Setup

1. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

2. **Running the WebSocket server**:
    - Navigate to the `/backend` folder and run the WebSocket server:

    ```bash
    python server.py
    ```

3. **MQTT Subscriber**:
    - Run the MQTT subscriber to listen for MQTT messages and control the relay:

    ```bash
    python mqtt_subscriber.py
    ```

### Frontend Setup

1. Open the `index.html` file in a browser to interact with the light scheduler interface. This is where you can set the ON and OFF times for the light.

### Arduino Setup

1. Open the Arduino IDE and load the `light_control.ino` code into your Arduino board (UNO or compatible).
2. Upload the code to your Arduino board.
3. Make sure your Arduino is connected to your system and the correct serial port is selected in the Arduino IDE.

## Usage

1. **Set Schedule**:
   - Use the **Web Interface** to set the ON and OFF times for the light.
   - Click **Set Schedule** to send the schedule to the WebSocket server.

2. **WebSocket Communication**:
   - The WebSocket server will forward the schedule to the MQTT broker.
   - The MQTT subscriber will receive the messages and send commands ('1' for ON, '0' for OFF) to the Arduino via serial communication.

3. **Arduino Control**:
   - The Arduino will receive the signals and control the relay accordingly, turning the light on or off.

## Example

- **ON Time**: 01:26 (Light turns ON at 01:26 PM)
- **OFF Time**: 01:27 (Light turns OFF at 01:27 PM)

## Screenshots

![Web Interface Screenshot](screenshots/web-interface.png)
*(A sample screenshot showing the light scheduler interface)*

## Demo

Here is a [short demo video](#) of the system in action, showing the web interface, WebSocket communication, and the light turning on and off based on the schedule.

## Contributing

Feel free to fork this project and contribute! Here are some ways you can help:

- Report any bugs or issues
- Suggest new features or improvements
- Improve documentation or add new demos

To contribute, simply fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed by IRASUBIZA SALY NELSON**  
Year 2C, Embedded Systems Assignment

