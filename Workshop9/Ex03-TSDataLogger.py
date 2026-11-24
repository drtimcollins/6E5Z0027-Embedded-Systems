from machine import Pin
import time
import json, urequests
import MyWifi
time.sleep(0.1) # Wait for USB to become ready

# You need to paste your own API write key here
WRITE_KEY = 'XXXXXXXXXXXXXXXXX'
uploadData = {'api_key': WRITE_KEY}

dataIn = Pin('GP17', Pin.IN)                   # GPIO input connected to button/switch

if MyWifi.connect():
    while True:
        uploadData['field1'] = dataIn.value()  # Field1 equals button 2 state.

        response = urequests.post('https://api.thingspeak.com/update.json',
                            headers={'Content-Type': 'application/json'},
                            data=json.dumps(uploadData))
        if response.status_code == 200:
            print("Post operation successful")
        else:
            print(f"HTTP post error: {response.status_code}")
        response.close()        

        waitTime = 30                          # Wait 30s before next transmissions
        while waitTime > 0:
            print('Sleep for 30 seconds ', end='\r')
            time.sleep(1)
            waitTime -= 1
        print('\nReady')
