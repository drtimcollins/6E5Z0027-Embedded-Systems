import urequests
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import MyWifi

def getWithParams(url, params):
    query = '&'.join([f'{p}={params[p]}' for p in params])
    return urequests.get(url+'?'+query)

if MyWifi.connect():
    response = getWithParams("https://api.open-meteo.com/v1/forecast",
                            params = {"latitude": 53.471,"longitude": -2.24,
                                      "current": "temperature_2m,wind_speed_10m",
                                      "models": "ukmo_seamless"})  

    if response.status_code == 200:
        forecast = response.json()                    # Form a dictionary from the response

        temp = forecast['current']['temperature_2m']               # Look up values
        wind = forecast['current']['wind_speed_10m']
        temp_unit = forecast['current_units']['temperature_2m']    # Look up units
        wind_unit = forecast['current_units']['wind_speed_10m']
        temp_unit = temp_unit.replace(chr(176),' ')     # Degree symbol is incompatible...

        i2c = I2C(1, sda=Pin('GP26'), scl=Pin('GP27'))  # Set up I2C interface
        display = SSD1306_I2C(64, 32, i2c)              # Create driver object

        display.text(f'{wind}{wind_unit}', 0, 6)
        display.text(f'{temp}{temp_unit}', 0, 18)

        display.show()                    # Call the show() method last to update display


