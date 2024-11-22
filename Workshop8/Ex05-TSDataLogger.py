from machine import Pin
import network, time
import secrets                     # Locally stored module containin SSID and KEY for WiFi
import json, urequests

# You need to paste your own API write key here
WRITE_KEY = 'XXXXXXXXXXXXXXXXX'

print("Connecting to WiFi.", end="")
wifi = network.WLAN(network.STA_IF)              # Create WiFi network object
wifi.active(True)
wifi.connect(secrets.SSID, secrets.KEY)          # Connect to specific WiFi network
while not wifi.isconnected():                    # Wait until connected
  print(".", end="")
  time.sleep(0.25)
print(" Connected")

uploadData = {'api_key': WRITE_KEY}

def sendData():
    response = urequests.post('https://api.thingspeak.com/update.json',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(uploadData))
    if response.status_code == 200:
        print("Post operation succesful")
    else:
        print(f"HTTP post error: {response.status_code}")

btn1 = Pin('GP17', Pin.IN)                      # GPIO inputs connected to buttons
btn2 = Pin('GP16', Pin.IN)

while True:
    if btn1.value():                            # Only post when button 1 is pressed
        uploadData['field1'] = btn2.value()     # Field1 equals button 2 state.
        sendData()                              # Calls function defined above to post data
        print('Sleep for 20 seconds')
        time.sleep(20)                          # Pause so we don't exceed posting limit
        print('Ready')
    else:                                       # If button 1 was not pressed, check again
        time.sleep(0.2)                         # in 200 ms.
