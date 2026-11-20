import time, urequests
import MyWifi
time.sleep(0.1) # Wait for USB to become ready


if MyWifi.connect():
    # Send API request to aisenseapi.com.
    # Returns a JSON object with the current date and time
    result = urequests.get('https://aisenseapi.com/services/v1/datetime')
    timeData = result.json()    
    print(timeData['datetime'])
    result.close()
