from machine import Pin
import network, time
import secrets                     # Locally stored module containin SSID and KEY for WiFi
import urequests

# You need to paste your own channel ID number (YYYYYYY) and API read key (ZZZZZZZZZZ)
CHANNEL_ID = 'YYYYYYY'
READ_KEY = 'ZZZZZZZZZZZZZZZZ'

led1 = Pin('GP19', Pin.OUT)            # Create input and output Pin objects
led2 = Pin('GP18', Pin.OUT)

print("Connecting to WiFi.", end="")
wifi = network.WLAN(network.STA_IF)              # Create WiFi network object
wifi.active(True)
wifi.connect(secrets.SSID, secrets.KEY)          # Connect to specific WiFi network
while not wifi.isconnected():                    # Wait until connected
  print(".", end="")
  time.sleep(0.25)
print(" Connected")

while True:
    try:                                    # Request just one result (the latest reading)
        response = urequests.get('https://api.thingspeak.com/channels/' + CHANNEL_ID + 
                             '/feeds.json?api_key=' + READ_KEY + '&results=1')
        if response.status_code == 200:     # HTTP status 200 = Successful request
            print("Request successful")
            data = response.json()
            print(f"Field 2 = {data['feeds'][0]['field2']}")
            if int(data['feeds'][0]['field2']) == 1:
                led1.off()                  # If field2 > 0, turn LED1 off, LED2 on
                led2.on()
            else:
                led1.on()                   # If field2 == 0, turn LED1 on, LED2 off
                led2.off()            
        else:
            print(f"HTTP request error: {response.status_code}")                    
    except:                             # Occasionally, get() can fail, when it does
        print("Request failed")         # just retry next time.
    time.sleep(2)                       # Wait 2 s before checking again
