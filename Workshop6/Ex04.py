from machine import Pin, Timer

led1 = Pin('GP19', Pin.OUT)            # Create input and output Pin objects
led2 = Pin('GP18', Pin.OUT)
btn1 = Pin('GP17', Pin.IN)
btn2 = Pin('GP16', Pin.IN)

def checkButtons(timer):               # Callback function
   if btn1.value() and btn2.value():   # LED 1 on if Button 1 AND Button 2 are pressed.
      led1.on()
   else:
      led1.off()
   if btn1.value() or btn2.value():    # LED 2 on if Button 1 OR Button 2 are pressed.
      led2.on()
   else:
      led2.off()           

# Set up a timer to trigger every 50 ms
tmr = Timer(period = 50, callback = checkButtons)