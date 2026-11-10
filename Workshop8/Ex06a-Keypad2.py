from keypad import Keypad          # Keypad driver module, replaces the key scanning code
from machine import Pin

def keyPressed(keyValue):
   print(keyValue, end="")         # When a key is pressed, just print it to the shell

# Setup keypad object with the correct pins and with keyPressed() as the callback function
kp = Keypad(rows = (Pin(26), Pin(22), Pin(21), Pin(20)),
            columns = (Pin(19), Pin(18), Pin(17), Pin(16)),
            callback = keyPressed)
