from machine import Pin, Timer

# Create tuple of the seven segment cathodes.
segs = (Pin('GP0',Pin.OUT), Pin('GP2',Pin.OUT), Pin('GP13',Pin.OUT), Pin('GP14',Pin.OUT),
        Pin('GP15',Pin.OUT), Pin('GP1',Pin.OUT), Pin('GP12',Pin.OUT))
# LED patterns for digits 0-9 (active low)
codes = [(0,0,0,0,0,0,1), (1,0,0,1,1,1,1), (0,0,1,0,0,1,0), (0,0,0,0,1,1,0),
         (1,0,0,1,1,0,0), (0,1,0,0,1,0,0), (0,1,0,0,0,0,0), (0,0,0,1,1,1,1),
         (0,0,0,0,0,0,0), (0,0,0,0,1,0,0)]

counter = 0                                   # counter variable to cycle through digits

def digitCounter(timer):
   global counter                             # global needed so we can change the value
   for i in range(7):
      segs[i].value(codes[counter][i])        # Look up LED states needed for this digit
   if counter < 9:                            # Increment or reset the counter
      counter = counter + 1
   else:
      counter = 0

tmr = Timer(period = 500, callback=digitCounter)