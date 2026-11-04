import urequests
import MyWifi

if MyWifi.connect():
    # Send API request to aisenseapi.com. Returns a JSON object with the current date/time
    result = urequests.get('https://aisenseapi.com/services/v1/datetime')
    timeData = result.json()
    print(timeData['datetime'])
