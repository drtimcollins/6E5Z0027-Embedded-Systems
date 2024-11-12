from machine import Pin, Timer, PWM

led1 = Pin('GP19', Pin.OUT)                # Create input and output Pin objects
led2 = Pin('GP18', Pin.OUT)
btn1 = Pin('GP17', Pin.IN, Pin.PULL_DOWN)  # Pin.PULL_DOWN enables internal pull-down
btn2 = Pin('GP16', Pin.IN, Pin.PULL_DOWN)  # resistors for the inputs.

def checkButtons(timer):                   # Callback function
   led1.value(btn1.value())                # Light LED1 if button 1 is pressed
   led2.value(btn2.value())                # Light LED2 if button 2 is pressed

# Set up a timer to trigger every 50 ms
tmr = Timer(period = 50, callback = checkButtons)
