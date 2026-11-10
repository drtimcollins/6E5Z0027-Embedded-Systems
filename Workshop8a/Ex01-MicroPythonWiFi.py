import network, time
import secrets                       # Locally stored module containin SSID and KEY for WiFi

print("Connecting to WiFi.", end="")
wifi = network.WLAN(network.STA_IF)              # Create WiFi network object
wifi.active(True)
wifi.connect(secrets.SSID, secrets.KEY)          # Connect to specific WiFi network
while not wifi.isconnected():                    # Wait until connected
  print(".", end="")
  time.sleep(0.25)
print(" Connected")

print(f"ESSID:     {wifi.config('essid')}")          # Show information about the network
print(f"Channel:   {wifi.config('channel')}")
print(f"TX Power:  {wifi.config('txpower')} dBm")
print(f"Host name: {wifi.config('hostname')}")
