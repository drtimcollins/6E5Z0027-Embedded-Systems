import time
from machine import Pin

led = Pin('LED', Pin.OUT)     # Create output Pin.

while True:                   # Condition is never False so this loops forever.
   led.toggle()               # Toggle LED state between on and off.
   time.sleep(0.5)            # Wait half a second between toggles.