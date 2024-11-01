import time
from machine import Pin

led1 = Pin('GP19', Pin.OUT)   # Create a Pin output on GP19
led2 = Pin('GP18', Pin.OUT)   # Create a Pin output on GP18

led1.on()                     # Switch led1 (GP19) on
time.sleep(1)                 # Pause for 1 second
led2.on()                     # Switch led2 (GP18) on
time.sleep(1)                 # Pause for 1 second
led1.off()                    # Switch led1 off
time.sleep(1)                 # Pause for 1 second
led2.off()                    # Switch led2 off