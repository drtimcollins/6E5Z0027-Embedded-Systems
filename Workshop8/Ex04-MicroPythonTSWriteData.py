import network, time
import secrets                     # Locally stored module containin SSID and KEY for WiFi
import json, urequests

# You need to paste your own API write key here
WRITE_KEY = 'XXXXXXXXXXXXXXXX'

print("Connecting to WiFi.", end="")
wifi = network.WLAN(network.STA_IF)              # Create WiFi network object
wifi.active(True)
wifi.connect(secrets.SSID, secrets.KEY)          # Connect to specific WiFi network
while not wifi.isconnected():                    # Wait until connected
  print(".", end="")
  time.sleep(0.25)
print(" Connected")

uploadData = {'api_key': WRITE_KEY, 'field1':0, 'field2':1}
response = urequests.post('https://api.thingspeak.com/update.json',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(uploadData))
if response.status_code == 200:        # HTTP status code 200 = successful request
    print("Post operation succesful")
else:
    print(f"HTTP post error: {response.status_code}")
