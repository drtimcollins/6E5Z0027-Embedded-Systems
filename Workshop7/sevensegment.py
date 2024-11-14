from machine import Pin, Timer

class SevenSegment:
   # LED patterns for digits 0-9 (active low)
   _codes = ((0,0,0,0,0,0,1), (1,0,0,1,1,1,1), (0,0,1,0,0,1,0), (0,0,0,0,1,1,0),
             (1,0,0,1,1,0,0), (0,1,0,0,1,0,0), (0,1,0,0,0,0,0), (0,0,0,1,1,1,1),
             (0,0,0,0,0,0,0), (0,0,0,0,1,0,0))

   def __init__(self, *, segments, digits):
      self._segs = segments
      self._digits = digits
      for p in segments+digits:
         p.init(Pin.OUT, value = 0)
      self._digitCount = 0                              # Which digit to update next.
      self._digitValues = [0,0,0,0]
      self._tmr = Timer(freq = 100, callback=self._updateDisplay)

   def setDigits(self, values):
      self._digitValues = values.copy()

   def _updateDisplay(self, timer):                     # Called 100 times per second
      self._digits[self._digitCount].off()              # Turn off anode
      self._digitCount = (self._digitCount + 1) % 4
      for i in range(7):                                # Set cathodes to show this digit
         self._segs[i].value(SevenSegment._codes[self._digitValues[self._digitCount]][i])
      self._digits[self._digitCount].on()               # Turn on anode to light the LEDs
