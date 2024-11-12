from keypad import Keypad
from machine import Pin

def keyPressed(keyValue):
   print(keyValue, end="")

kp = Keypad(rows = (Pin(26), Pin(22), Pin(21), Pin(20)),
            columns = (Pin(19), Pin(18), Pin(17), Pin(16)),
            callback = keyPressed)
