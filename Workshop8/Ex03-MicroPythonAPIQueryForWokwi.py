""" 
Note: Wokwi Wifi does not work with the latest MicroPython firmware.
To run this code in a simulation, you need to edit the diagram.json file
and replace the line:
      "attrs": { "env": "micropython-20231227-v1.22.0"}
with
      "attrs": { "env": "micropython-20230426-v1.20.0"}
"""
import network, time, urequests

time.sleep(0.1) # Wait for USB to become ready

print("Connecting to WiFi.", end="")
wifi = network.WLAN(network.STA_IF)              # Create WiFi network object
wifi.active(True)
wifi.connect('Wokwi-GUEST')
while not wifi.isconnected():                    # Wait until connected
  print(".", end="")
  time.sleep(0.25)
print(" Connected")

# Send API request to timeapi.io. Returns a JSON object with the current date and time
result = urequests.get('https://timeapi.io/api/time/current/zone?timeZone=Europe%2FLondon')
timeData = result.json()
print(timeData['dateTime'])
