from keypad import Keypad
from machine import Pin

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
kp = Keypad(rows = (Pin(26), Pin(22), Pin(21), Pin(20)),
            columns = (Pin(19), Pin(18), Pin(17), Pin(16)),
            callback = keyPressed)