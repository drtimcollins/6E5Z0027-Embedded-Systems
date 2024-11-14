from max7219 import DotMatrix         # Import the DotMatrix driver
from machine import Pin, SPI
import time

spi = SPI(0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))   # Intialize the SPI
ss = Pin(5)                                          # Create CS pin
display = DotMatrix(spi, ss, 4, True) # Create MAX7129 DotMatrix driver for 4 displays
display.setBrightness(10)             # Needed in real-life (virtual display ignores this)

while True:
    display.fill(0)                    # Clear the display (all black)
    display.ellipse(5,3,3,3,1,True)    # Draw a circle at (5,3), radius = 3, colour = 1
    display.hline(3,3,5,0)             # Horizontal line at (3,3), len=5, colour=0 (off)
    display.text("12",13,0)            # Display text at (13,0)
    display.show()                     # Call the show() method last to update display
    time.sleep(1)

    display.fill(0)                    # Clear the display (all black)
    display.ellipse(5,3,3,3,1,True)    # Draw a circle at (5,3), radius = 3, colour = 1
    display.vline(5,1,5,0)             # Vertical line at (5,1), len=5, colour=0 (off)
    display.text("34",13,0)            # Display text at (13,0)
    display.show()                     # Call the show() method last to update display
    time.sleep(1)

