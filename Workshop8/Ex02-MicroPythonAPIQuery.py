import network, time, urequests
import secrets                       # Locally stored module containin SSID and KEY for WiFi

print("Connecting to WiFi.", end="")
wifi = network.WLAN(network.STA_IF)              # Create WiFi network object
wifi.active(True)
wifi.connect(secrets.SSID, secrets.KEY)          # Connect to specific WiFi network
while not wifi.isconnected():                    # Wait until connected
  print(".", end="")
  time.sleep(0.25)
print(" Connected")

# Send API request to timeapi.io. Returns a JSON object with the current date and time
result = urequests.get('https://timeapi.io/api/time/current/zone?timeZone=Europe%2FLondon')
timeData = result.json()
print(timeData['dateTime'])
