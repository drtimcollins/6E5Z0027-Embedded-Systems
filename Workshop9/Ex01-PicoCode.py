# MicroPython script for the Smart Heating Example Demonstration
from machine import Pin, Timer, ADC
import network, time, urequests, json
import secrets  				# Locally stored module contains WiFi and ThingSpeak keys

print("Connecting to WiFi.", end="")
wifi = network.WLAN(network.STA_IF) 			# Create WiFi network object
wifi.active(True)
wifi.connect(secrets.SSID, secrets.KEY) 		# Connect to specific WiFi network
while not wifi.isconnected():					# Wait until connected
    print(".", end="")
    time.sleep(0.25)
print(" Connected")

enabledLED = Pin('GP19', Pin.OUT) 		# Create LED output Pin objects
boilerLED  = Pin('GP18', Pin.OUT)
tempAdc = ADC('GP26')   				# Setup ADC0 as temperature sensor input
state = {'Target Temperature': 20, 'isHeatingEnabled': True,
         'timeSinceLastPost': 1000, 'lastID': 0}
uploadData = {'api_key': secrets.WRITE_KEY}

def updateHeating(timer):
    newTemperature = int(tempAdc.read_u16() / 397)			# Read ADC to get temperature.
    print(f"Current Temperature = {newTemperature}\u00B0C")
    if newTemperature < state['Target Temperature'] and state['isHeatingEnabled']:
        isBoilerOn = True
    else:
        isBoilerOn = False
    boilerLED.value(isBoilerOn)

    # Check for new data
    response = urequests.get('https://api.thingspeak.com/channels/' +
                             secrets.CHANNEL_ID + '/feeds.json?api_key=' +
                             secrets.READ_KEY + '&minutes=2').json()
    print(f"{len(response['feeds'])} received.")
    for feed in response['feeds']:
        if feed['entry_id'] > state['lastID']:		# Not seen this entry yet
            state['lastID'] = feed['entry_id']
            if feed['field1'] is not None:			# Skip empty feeds
                state['isHeatingEnabled'] = (feed['field1'] == 'True')
                enabledLED.value(state['isHeatingEnabled'])
            if feed['field4'] is not None:
                state['Target Temperature'] = int(feed['field4'])
            print('State updated')					# Show new state data

    # Post new data once every 30s
    state['timeSinceLastPost'] = state['timeSinceLastPost'] + 1
    if state['timeSinceLastPost'] > 15:				# Send update every 30s        
        uploadData['field2'] = 'True' if isBoilerOn else 'False'
        uploadData['field3'] = newTemperature
        response = urequests.post('https://api.thingspeak.com/update.json',
                       headers={'Content-Type': 'application/json'},
                       data=json.dumps(uploadData))
        if response.status_code == 200:
            print("Post operation succesful")
            state['timeSinceLastPost'] = 0			# Reset counter if successful

tmr = Timer(period=2000, callback=updateHeating)
