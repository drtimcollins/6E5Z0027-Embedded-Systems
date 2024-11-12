from keypad import Keypad
from machine import Pin

secretCode = '31415927'
isLocked = False
inbuffer = ""

print("State = UNLOCKED")

def keyPressed(keyValue):
   global isLocked, inbuffer
   if isLocked:
      if keyValue == '#':
         if checkCode():
            isLocked = False
            print(" - Correct, State = UNLOCKED")
         else:
            print(" - Incorrect code.")
         inbuffer = ""
      else:
         inbuffer = inbuffer + keyValue
         print(keyValue, end="")
   else:
      if keyValue == '*':
         isLocked = True
         print("State = LOCKED")

def checkCode():
   if len(inbuffer) < 8:
      return False
   return (inbuffer[-8:] == secretCode)  

kp = Keypad(rows = (Pin(26), Pin(22), Pin(21), Pin(20)),
            columns = (Pin(19), Pin(18), Pin(17), Pin(16)),
            callback = keyPressed)
