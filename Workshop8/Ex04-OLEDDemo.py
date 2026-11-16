from machine import Pin, I2C
from ssd1306 import SSD1306_I2C                   # Import SSD1306 I2C display driver
import time
time.sleep(0.1)

i2c = I2C(1, sda=Pin('GP26'), scl=Pin('GP27'))    # Set up I2C
display = SSD1306_I2C(128, 64, i2c)               # Create display 128x64 pixels

display.text("Hello World",20,0)        # Display text at (20,0)
display.text("================",0,8)    # Display text at (0,8)
display.text("On a 128 x 64",12,16)     # Display text at (12,16)
display.text("pixel display we",0,24)   # Display text at (0,24)
display.text("can show 8 lines",0,32)   # Display text at (0,32)
display.text("of text, with up",0,40)   # Display text at (0,40)
display.text("to 16 chars each",0,48)   # Display text at (0,48)
display.text("0123456789ABCDEF",0,56)   # Display text at (0,56)

display.show()