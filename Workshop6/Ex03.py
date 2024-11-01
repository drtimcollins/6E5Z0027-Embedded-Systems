from machine import Pin, Timer

led = Pin('LED', Pin.OUT)     # Create output Pin.

def toggleLED(timer):         # Callback function is passed the calling Timer object
   led.toggle()               # Toggle LED state between on and off.

# Set up a timer to trigger every 500 ms and call the toggleLED function (above).
tmr = Timer(period = 500, callback = toggleLED)