# MicroPython script for the Smart Heating Example Demonstration
# Connections: GP20 - Temperature sensor (DS18B20)
#              GP18 - Boiler relay
#              GP19 - Heating-enabled indicator
# Requires valid WiFi and ThingSpeak credentials in MyKeys module.
from machine import Pin, Timer
from onewire import OneWire
from ds18x20 import DS18X20
import time, urequests, json
import MyWifi, MyKeys  		# Locally stored module contains WiFi and ThingSpeak keys
time.sleep(0.1) # Wait for USB to become ready

enabledLED = Pin('GP19', Pin.OUT) 		# Create LED output Pin objects
boilerRelay  = Pin('GP18', Pin.OUT)
tempSensor = DS18X20(OneWire(Pin('GP20'))) 
tempSensorID = tempSensor.scan()[0]
targetTemperature = 20
isHeatingEnabled =  True
timeSinceLastPost = 1000                # Counter to limit posting rate
lastID = 0                              # Keeps track of fields already seen
uploadData = {'api_key': MyKeys.WRITE_KEY}

if MyWifi.connect(30):
    while True:
        tempSensor.convert_temp()              # Initiate temperature reading
        time.sleep(1)                               # Wait for sensor...
        newTemperature = tempSensor.read_temp(tempSensorID)
        print(f"Current Temperature = {newTemperature}\u00B0C")
        print(f"Target Temperature = {targetTemperature}\u00B0C")    
        # Boiler control logic:
        if newTemperature < targetTemperature and isHeatingEnabled:
            isBoilerOn = True
        else:
            isBoilerOn = False
        boilerRelay.value(isBoilerOn)

        # Post new data to ThingSpeak once every 30s
        timeSinceLastPost = timeSinceLastPost + 10
        if timeSinceLastPost >= 30:				# Send update every 30s        
            print('Posting...')
            uploadData['field2'] = 'True' if isBoilerOn else 'False'
            uploadData['field3'] = newTemperature
            response = urequests.post('https://api.thingspeak.com/update.json',
                        headers={'Content-Type': 'application/json'},
                        data=json.dumps(uploadData))
            if response.status_code == 200 and response.json() != 0:
                print("Post operation successful")
                timeSinceLastPost = 0			# Reset counter if successful
                response.close()
        else:
            print('Getting...')
            # If we didn't post, check for new data from ThingSpeak instead
            response = urequests.get('https://api.thingspeak.com/channels/' +
                                    MyKeys.CHANNEL_ID + '/feeds.json?api_key=' +
                                    MyKeys.READ_KEY + '&minutes=2')
            print(f"{len(response.json()['feeds'])} feeds received.")
            for feed in response.json()['feeds']:
                if feed['entry_id'] > lastID:	    	# Not seen this entry yet
                    lastID = feed['entry_id']
                    if feed['field1'] is not None:			# Skip empty feeds
                        isHeatingEnabled = (feed['field1'] == 'True')
                        enabledLED.value(isHeatingEnabled)
                    if feed['field4'] is not None:
                        targetTemperature = int(feed['field4'])
                    print('State updated')
            response.close()
        print('Get/Post done')
        time.sleep(10)                  # Wait 10s before next get or post
