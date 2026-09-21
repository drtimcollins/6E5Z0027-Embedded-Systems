import urequests
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
        for k in forecast:
            print(f'{k}: {forecast[k]}')
