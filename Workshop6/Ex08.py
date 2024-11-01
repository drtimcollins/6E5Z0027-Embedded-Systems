from machine import Pin, Timer, PWM

pwmLed = PWM('GP19', freq=1000)        # Create PWM object for the LED
pwmScope = PWM('GP0', freq=1000)       # and another for the scope.
btn1 = Pin('GP17', Pin.IN)             # Set up input pins for buttons 1 & 2
btn2 = Pin('GP16', Pin.IN)

def setPWM(value):
   pwmLed.duty_u16(value)              # Send the same PWM signal to the
   pwmScope.duty_u16(value)            # scope and the LED.

def checkButtons(timer):               # Callback function
   if btn1.value():
       setPWM(0x4000)                  # Set to 25%
   elif btn2.value():
       setPWM(0xC000)                  # Set to 75%
   else:      
       setPWM(0x8000)                  # Set to 50%

# Set up a timer to trigger every 50 ms
tmr = Timer(period = 50, callback = checkButtons)