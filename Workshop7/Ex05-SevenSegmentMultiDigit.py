from machine import Pin, Timer

# Create tuple of the seven segment cathodes.
segs = (Pin('GP0',Pin.OUT), Pin('GP2',Pin.OUT), Pin('GP13',Pin.OUT), Pin('GP14',Pin.OUT),
        Pin('GP15',Pin.OUT), Pin('GP1',Pin.OUT), Pin('GP12',Pin.OUT))
# Seven Segment Anodes.
digits = (Pin('GP3', Pin.OUT), Pin('GP4', Pin.OUT),
          Pin('GP5', Pin.OUT), Pin('GP11', Pin.OUT))
# LED patterns for digits 0-9 (active low)
codes = [(0,0,0,0,0,0,1), (1,0,0,1,1,1,1), (0,0,1,0,0,1,0), (0,0,0,0,1,1,0),
         (1,0,0,1,1,0,0), (0,1,0,0,1,0,0), (0,1,0,0,0,0,0), (0,0,0,1,1,1,1),
         (0,0,0,0,0,0,0), (0,0,0,0,1,0,0)]

counter = [0, 1, 2, 3]                           # Four counters, one for each digit

def numberCounter(timer):                        # Called once per second
   for i in range(4):                            
      counter[i] = (counter[i] + 1) % 10         # Increment or reset each digit

digitCount = 0                                   # Which digit to update next.
def updateDisplay(timer):                        # Called 100 times per second
   global digitCount
   digits[digitCount].off()                      # Turn off anode
   digitCount = (digitCount + 1) % 4             # Step to the next digit       
   for i in range(7):                            # Set cathodes to show this digit
      segs[i].value(codes[counter[digitCount]][i])
   digits[digitCount].on()                       # Turn on anode to light the LEDs


tmr1 = Timer(period = 1000, callback=numberCounter)   # Slow timer, updates conter
tmr2 = Timer(freq = 100, callback=updateDisplay)      # Fast timer, strobes the digits
