import asyncio
import websockets
import subprocess
import json
from datetime import datetime

schedule = {}

async def handle_client(websocket):
    global schedule
    async for message in websocket:
        print("Received:", message)
        schedule = json.loads(message)
        await websocket.send("Schedule received!")

async def scheduler():
    global schedule
    sent = set()
    while True:
        now = datetime.now().strftime("%H:%M")
        if schedule:
            if now == schedule.get('on') and 'on' not in sent:
                print(f"Time {now}: Sending ON command")
                subprocess.run([
                    "mosquitto_pub",
                    "-h", "localhost",
                    "-t", "relay",
                    "-m", "ON"
                ])
                sent.add('on')

            if now == schedule.get('off') and 'off' not in sent:
                print(f"Time {now}: Sending OFF command")
                subprocess.run([
                    "mosquitto_pub",
                    "-h", "localhost",
                    "-t", "relay",
                    "-m", "OFF"
                ])
                sent.add('off')

        await asyncio.sleep(1)

async def main():
    ws_server = await websockets.serve(handle_client, "0.0.0.0", 8765)
    await asyncio.gather(scheduler())

if __name__ == "__main__":
    asyncio.run(main())
