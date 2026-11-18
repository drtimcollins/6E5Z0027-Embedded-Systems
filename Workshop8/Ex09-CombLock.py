from keypad import Keypad
from machine import Pin
import time
time.sleep(0.1)

secretCode = '31415927'
isLocked = False
inbuffer = "--------"

print("State = UNLOCKED")

def keyPressed(keyValue):
   global isLocked, inbuffer           # Global variables are stored between function calls
   if isLocked:
      if keyValue == '#':              # User is trying to unlock
         if inbuffer == secretCode:    # Success only if the code matches
            isLocked = False
            print(" - Correct, State = UNLOCKED")
         else:
            print(" - Incorrect code.")
         inbuffer = "--------"                  # Wrong code so reset the buffer
      else:                                     # New number needs storing in the buffer:
         inbuffer = inbuffer[1:] + keyValue     # Move buffer to the left and add new value
         print(keyValue, end="")
   elif keyValue == '*':                        # Unlocked and '*' pressed so change the 
      isLocked = True                           # state to locked.
      print("State = LOCKED")

# Setup keypad object with the correct pins and with keyPressed() as the callback function
kp = Keypad(rows = (Pin(15), Pin(14), Pin(13), Pin(12)),
            columns = (Pin(11), Pin(10), Pin(9), Pin(8)),
            callback = keyPressed)