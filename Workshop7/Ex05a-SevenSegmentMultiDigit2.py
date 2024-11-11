from sevensegment import SevenSegment
from machine import Pin, Timer

display = SevenSegment((Pin('GP0'), Pin('GP2'), Pin('GP13'), Pin('GP14'), 
                        Pin('GP15'), Pin('GP1'), Pin('GP12')), 
                        (Pin('GP3'), Pin('GP4'), Pin('GP5'), Pin('GP11')))

counter = [0, 1, 2, 3]                           # Four counters, one for each digit
display.setDigits(counter)

def numberCounter(timer):                        # Called once per second
   for i in range(4):                            
      if counter[i] < 9:                         # Increment or reset each element of
         counter[i] = counter[i] + 1             # counter list.
      else:
         counter[i] = 0
   display.setDigits(counter)

tmr = Timer(period = 1000, callback=numberCounter)   # Slow timer, updates conter
