from keypad import Keypad          # Keypad driver module, replaces the key scanning code
from machine import Pin
import time
time.sleep(0.1)

def keyPressed(keyValue):
   print(keyValue, end="")         # When a key is pressed, just print it to the shell

# Setup keypad object with the correct pins and with keyPressed() as the callback function
kp = Keypad(rows = (Pin(15), Pin(14), Pin(13), Pin(12)),
            columns = (Pin(11), Pin(10), Pin(9), Pin(8)),
            callback = keyPressed)
