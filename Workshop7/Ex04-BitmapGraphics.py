from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from framebuf import FrameBuffer, MONO_HMSB

i2c = I2C(1, sda=Pin('GP26'), scl=Pin('GP27'))  # Set up I2C interface
display = SSD1306_I2C(64, 32, i2c)              # Create a driver object for 64x32 display

imgHMSB = bytearray(b'\x00\x1c\x00\x00"\x00\x00A\x00\x80\x80\x00\x80\x80\x00\x80\x80'
    b'\x00\x80\xe3\x00x\x14\x0f\x10\x08\x04\x10\x08\x04 \x08\x02 \x08\x028\x1c\x0e'
    b'\xc4\xe3\x11\x02A \x82\x80 \x82\x80 \x82\x80 Dc\x118\x14\x0e\x00\x08\x00\x00'
    b'\x08\x00\x00\x00\x00')
imgBuf = FrameBuffer(imgHMSB, 24, 23, MONO_HMSB)

display.blit(imgBuf,4,4)
display.text('Man', 32,2)
display.text('Met', 32,12)
display.text('Eng', 32,22)

display.show()                    # Call the show() method last to update display
