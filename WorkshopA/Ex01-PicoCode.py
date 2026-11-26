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

# Class to encapsulate all code associated with this application
class SmartHeaterPico:
    def __init__(self):
        self.enabledLED = Pin('GP19', Pin.OUT) 		# Create LED output Pin objects
        self.boilerRelay  = Pin('GP18', Pin.OUT)
        self.tempSensor = DS18X20(OneWire(Pin('GP20'))) 
        self.tempSensorID = self.tempSensor.scan()[0]
        self.targetTemperature = 20
        self.isHeatingEnabled =  True
        self.timeSinceLastPost = 1000               # Counter to limit posting rate
        self.lastID = 0                             # Keeps track of fields already seen
        self.uploadData = {'api_key': MyKeys.WRITE_KEY}
        self.tmr = Timer(period=10000, callback=self.updateHeating)

    # Called every ten seconds to update the system, get data, and post data when needed
    def updateHeating(self, timer):
        self.tempSensor.convert_temp()              # Initiate temperature reading
        time.sleep(1)                               # Wait for sensor...
        newTemperature = self.tempSensor.read_temp(self.tempSensorID)
        print(f"Current Temperature = {newTemperature}\u00B0C")
        print(f"Target Temperature = {self.targetTemperature}\u00B0C")    
        # Boiler control logic:
        if newTemperature < self.targetTemperature and self.isHeatingEnabled:
            isBoilerOn = True
        else:
            isBoilerOn = False
        self.boilerRelay.value(isBoilerOn)

        # Post new data to ThingSpeak once every 30s
        self.timeSinceLastPost = self.timeSinceLastPost + 10
        if self.timeSinceLastPost > 30:				# Send update every 30s        
            self.uploadData['field2'] = 'True' if isBoilerOn else 'False'
            self.uploadData['field3'] = newTemperature
            response = urequests.post('https://api.thingspeak.com/update.json',
                        headers={'Content-Type': 'application/json'},
                        data=json.dumps(self.uploadData))
            if response.status_code == 200 and response.json() != 0:
                print("Post operation successful")
                self.timeSinceLastPost = 0			# Reset counter if successful
        else:
            # If we didn't post, check for new data from ThingSpeak instead
            response = urequests.get('https://api.thingspeak.com/channels/' +
                                    MyKeys.CHANNEL_ID + '/feeds.json?api_key=' +
                                    MyKeys.READ_KEY + '&minutes=2').json()
            print(f"{len(response['feeds'])} feeds received.")
            for feed in response['feeds']:
                if feed['entry_id'] > self.lastID:	    	# Not seen this entry yet
                    self.lastID = feed['entry_id']
                    if feed['field1'] is not None:			# Skip empty feeds
                        self.isHeatingEnabled = (feed['field1'] == 'True')
                        self.enabledLED.value(self.isHeatingEnabled)
                    if feed['field4'] is not None:
                        self.targetTemperature = int(feed['field4'])
                    print('State updated')
        response.close()

if MyWifi.connect():
    sh = SmartHeaterPico()
