from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C
import time

# using default address 0x3C
i2c = I2C(1, sda=Pin('GP26'), scl=Pin('GP27'))
display = SSD1306_I2C(128, 64, i2c)

while True:
    display.fill(0)                    # Clear the display (all black)
    display.ellipse(23,32,12,12,1,True)# Draw a circle at (23,32), radius = 12
    display.rect(12,30,23,5,0,True)    # Rectangle at (3,3) size=23x5, colour=0 (off)
    display.text("12345678",50,20)     # Display text at (13,0)
    display.text("Locked",50,38)
    display.show()                     # Call the show() method last to update display
    time.sleep(1)

    display.fill(0)                    # Clear the display (all black)
    display.ellipse(23,32,12,12,1,True)# Draw a circle at (23,32), radius = 12
    display.rect(21,21,5,23,0,True)    # Rectangle at (3,3) size=23x5, colour=0 (off)    
    display.text("31415927",50,20)     # Display text at (13,0)
    display.text("Unlocked",50,38)
    display.show()                     # Call the show() method last to update display
    time.sleep(1)

