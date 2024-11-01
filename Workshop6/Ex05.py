from machine import Pin, Timer

states = ('off', 'on')                 # A tuple that we will use to interpret Pin values

btn1 = Pin('GP17', Pin.IN)             # Create two button input Pin objects
btn2 = Pin('GP16', Pin.IN)

def printButtonState(timer):                        # Callback function    
   print("Button 1 is " + states[btn1.value()])     # Print button states using value() to
   print("Button 2 is " + states[btn2.value()])     # look up the text in the states tuple.

# Set up a timer to trigger every 500 ms
tmr = Timer(period = 500, callback = printButtonState)