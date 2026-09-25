import MyWifi

if MyWifi.connect():
    wifi = MyWifi.wlan

    print(f"ESSID:     {wifi.config('essid')}")       # Show information about the network
    print(f"Channel:   {wifi.config('channel')}")
    print(f"TX Power:  {wifi.config('txpower')} dBm")
    print(f"Host name: {wifi.config('hostname')}")
