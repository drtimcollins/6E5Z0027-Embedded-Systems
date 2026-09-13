from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, sda=Pin('GP26'), scl=Pin('GP27'))  # Set up I2C interface
display = SSD1306_I2C(64, 32, i2c)              # Create a driver object for 64x32 display

display.hline(17, 10, 29, 1)      # Horizontal line starting at (17,10) length=29, colour=1 
display.hline(17, 20, 29, 1)      # Horizontal line starting at (17,20) length=29, colour=1 
display.vline(26, 1, 29, 1)       # Vertical line starting at (26,1) length=29, colour=1 
display.vline(36, 1, 29, 1)       # Vertical line starting at (36,1) length=29, colour=1 

display.line(28, 2, 34, 8, 1)     # Line from (28,2) to (34,8) colour=1
display.line(34, 2, 28, 8, 1)     # Line from (34,2) to (28,8) colour=1
display.ellipse(31, 15, 3, 3, 1)  # Ellipse centred at (31,15), both radii=3 (i.e. a circle)
display.ellipse(41, 25, 3, 3, 1)  # Ellipse centred at (41,25), both radii=3 (i.e. a circle)

display.show()                    # Call the show() method last to update display
