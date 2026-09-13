from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C

i2c = I2C(1, sda=Pin('GP26'), scl=Pin('GP27'))  # Set up I2C interface
display = SSD1306_I2C(64, 32, i2c)              # Create a driver object for 64x32 display

level = 0                                  # Variable used to store the 'battery' level

def updateDisplay(timer):
    global level
    display.fill(0)                        # Clear the display (all black)
    level = (level + 20) % 120             # Advance level by 20, wrap around beyond 100
    
    display.rect(17,2,28,12,1)             # Battery icon outline
    display.rect(45,5,2,6,1,True)

    for n in range(level//20):             # Draw an extra rectangle for each 20% of level
        display.rect(19+n*5,4,4,8,1,True)  # Filled rectangles representing battery level

    display.text(f'{level}%', 17,20)       # Display the level in text too
    
    display.show()                         # Call the show() method last to update display

# Set up a timer to trigger every second
tmr = Timer(freq = 1, callback = updateDisplay)
