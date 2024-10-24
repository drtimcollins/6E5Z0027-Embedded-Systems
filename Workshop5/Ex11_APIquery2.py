import requests
# Query parameters are location info, data type requested, and duration of forecast
response = requests.get("https://api.open-meteo.com/v1/forecast",
                        params = {"latitude": 53.471,"longitude": -2.24,
                                  "hourly": "temperature_2m,precipitation",
                                  "forecast_days": 1, "models": "ukmo_seamless"})

if response.ok:
   forecast = response.json()                    # Form a dictionary from the response
   temp_unit = forecast['hourly_units']['temperature_2m']    # Look up units
   prec_unit = forecast['hourly_units']['precipitation']
   for i in range(len(forecast['hourly']['time'])):          # Step through the forecast
       time = forecast['hourly']['time'][i]                  # and print data.
       temp = forecast['hourly']['temperature_2m'][i]
       prec = forecast['hourly']['precipitation'][i]
       print(f"{time} - {temp}{temp_unit}, {prec} {prec_unit}")
       