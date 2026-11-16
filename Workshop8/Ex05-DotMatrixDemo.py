from max7219 import DotMatrix         # Import the DotMatrix driver
from machine import Pin, SPI
import time
time.sleep(0.1)

spi = SPI(0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))   # Intialize the SPI
cs = Pin(5)                                          # Create CS pin
display = DotMatrix(spi, cs, 4, True) # Create MAX7129 DotMatrix driver for 4 displays
display.setBrightness(10)             # Needed in real-life (virtual display ignores this)

x = 0
while True:
    display.fill(0)                      # Clear the display (all black)
    display.text('Hello World', 32-x, 0) # Show text at current scroll position
    display.show()                       # Call the show() method last to update display
    x += 1                               # Update by one pixel...
    if x > 120:                          # ...resetting if message has completed.
        x = 0

    time.sleep(0.05)

