from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, sda=Pin('GP26'), scl=Pin('GP27'))  # Set up I2C interface
display = SSD1306_I2C(64, 32, i2c)              # Create a driver object for 64x32 display

display.text('Hello', 12, 6)      # Write 'Hello' to the display buffer at coords (12,6)
display.text('World', 12, 18)     # Write 'World' to the display buffer at coords (12,18)

display.show()                    # Call the show() method last to update display
