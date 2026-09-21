from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, sda=Pin('GP26'), scl=Pin('GP27'))  # Set up I2C interface
display = SSD1306_I2C(64, 32, i2c)              # Create a driver object for 64x32 display

display.ellipse(32, 15, 15, 15, 1, True)   # Filled yellow circle
display.rect(26, 20, 12, 3, 0, True)       # Filled black rectangle
display.ellipse(26, 10, 3, 3, 0, True)     # Filled black circle
display.ellipse(38, 10, 3, 3, 0, True)     # Filled black circle

display.show()

