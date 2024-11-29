# MicroPython script for the Smart Heating Example Demonstration
# Connections: GP26 - Analogue temperature sensor (TMP37)
#              GP18 - Boiled on indicator
#              GP19 - Heating enabled indicator
# Requires valid WiFi and ThingSpeak credentials in mykeys module.
from machine import Pin, Timer, ADC
import network, time, urequests, json
import mykeys  				# Locally stored module contains WiFi and ThingSpeak keys

# Connect to WiFi network using credentials from mykeys
print("Connecting to WiFi.", end="")
wifi = network.WLAN(network.STA_IF) 			# Create WiFi network object
wifi.active(True)
wifi.connect(mykeys.SSID, mykeys.KEY) 		# Connect to specific WiFi network
while not wifi.isconnected():					# Wait until connected
    print(".", end="")
    time.sleep(0.25)
print(" Connected")

# Class to encapsulate all code associated with this application
class SmartHeaterPico:
    def __init__(self):
        self.enabledLED = Pin('GP19', Pin.OUT) 		# Create LED output Pin objects
        self.boilerLED  = Pin('GP18', Pin.OUT)
        self.tempAdc = ADC('GP26')   				# Setup ADC0 as temperature input
        self.targetTemperature = 20
        self.isHeatingEnabled =  True
        self.timeSinceLastPost = 1000               # Counter to limit posting rate
        self.lastID = 0                             # Keeps track of fields already seen
        self.uploadData = {'api_key': mykeys.WRITE_KEY}
        self.tmr = Timer(period=2000, callback=self.updateHeating)

    # Called every two seconds to update the system, get data, and post data when needed
    def updateHeating(self, timer):
        newTemperature = int(self.tempAdc.read_u16() / 397)			# Read temperature ADC
        print(f"Current Temperature = {newTemperature}\u00B0C")
        print(f"Target Temperature = {self.targetTemperature}\u00B0C")    
        # Boiler control logic:
        if newTemperature < self.targetTemperature and self.isHeatingEnabled:
            isBoilerOn = True
        else:
            isBoilerOn = False
        self.boilerLED.value(isBoilerOn)

        # Check for new data from ThingSpeak server
        response = urequests.get('https://api.thingspeak.com/channels/' +
                                mykeys.CHANNEL_ID + '/feeds.json?api_key=' +
                                mykeys.READ_KEY + '&minutes=2').json()
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

        # Post new data to ThingSpeak once every 30s
        self.timeSinceLastPost = self.timeSinceLastPost + 2
        if self.timeSinceLastPost > 30:				# Send update every 30s        
            self.uploadData['field2'] = 'True' if isBoilerOn else 'False'
            self.uploadData['field3'] = newTemperature
            response = urequests.post('https://api.thingspeak.com/update.json',
                        headers={'Content-Type': 'application/json'},
                        data=json.dumps(self.uploadData))
            if response.status_code == 200 and response.json() != 0:
                print("Post operation succesful")
                self.timeSinceLastPost = 0			# Reset counter if successful

sh = SmartHeaterPico()
