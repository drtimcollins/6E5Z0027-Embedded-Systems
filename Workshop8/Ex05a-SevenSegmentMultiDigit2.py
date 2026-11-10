from sevensegment import SevenSegment   # All the display driver code is now in this module
from machine import Pin, Timer

# Initialise display driver with segment and digit driver pins.
display = SevenSegment(segments = (Pin('GP0'), Pin('GP2'), Pin('GP13'), Pin('GP14'), 
                                   Pin('GP15'), Pin('GP1'), Pin('GP12')), 
                       digits = (Pin('GP3'), Pin('GP4'), Pin('GP5'), Pin('GP11')))

counter = [0, 1, 2, 3]                           # Four counters, one for each digit
display.setDigits(counter)

def numberCounter(timer):                        # Called once per second
   for i in range(4):                            
      counter[i] = (counter[i] + 1) % 10         # Increment or reset each digit
   display.setDigits(counter)

tmr = Timer(period = 1000, callback=numberCounter)   # Update counter
