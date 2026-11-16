import time
from machine import Pin, I2C
from rp2_lcd import I2cLcd
time.sleep(0.1) # Wait for USB to become ready

# Initialize I2C and LCD objects
i2c = I2C(1, scl=Pin('GP27'), sda=Pin('GP26'))
lcd = I2cLcd(i2c, 0x27, 2, 16)

lcd.putstr("LCD Display")        # Display at top-left if unspecified
lcd.move_to(0, 1)                # Move to column 0, row 1
lcd.putstr("0123456789ABCDEF")   # 16 characters - fills the display width
