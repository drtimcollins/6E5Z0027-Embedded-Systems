import urequests
import MyWifi

if MyWifi.connect():
    response = urequests.get("https://httpbin.org/ip")

    if response.status_code == 200:
        data = response.json()                    # Form a dictionary from the response
        print(f"\nResponse received: {data}")
