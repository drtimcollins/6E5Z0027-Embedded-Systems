import time
import json, urequests
import MyWifi
time.sleep(0.1) # Wait for USB to become ready

# You need to paste your own API write key here
WRITE_KEY = 'XXXXXXXXXXXXXXXX'

if MyWifi.connect():
    uploadData = {'api_key': WRITE_KEY, 'field1':0, 'field2':1}
    response = urequests.post('https://api.thingspeak.com/update.json',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps(uploadData))
    if response.status_code == 200:        # HTTP status code 200 = successful request
        print("Post operation succesful")
    else:
        print(f"HTTP post error: {response.status_code}")
    response.close()
