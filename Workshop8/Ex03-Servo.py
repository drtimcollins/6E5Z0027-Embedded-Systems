from machine import Pin, Timer, PWM

led1 = Pin('GP19', Pin.OUT)               # Create input and output Pin objects
led2 = Pin('GP18', Pin.OUT)
btn1 = Pin('GP17', Pin.IN, Pin.PULL_DOWN)
btn2 = Pin('GP16', Pin.IN, Pin.PULL_DOWN)
pwm = PWM('GP27',freq = 50)               # PWM output to control servo position

def checkButtons(timer):                  # Callback function
   led1.value(btn1.value())               # LEDs indicate buttons pressed
   led2.value(btn2.value())
   if btn2.value():
      pwm.duty_u16(8050)                  # On-time = 2.46ms => 180 degrees
   elif btn1.value():
      pwm.duty_u16(4825)                  # On-time = 1.47ms => 90 degrees
   else:
      pwm.duty_u16(1600)                  # On-time = 0.49ms => 0 degrees

# Set up a timer to trigger every 100 ms
tmr = Timer(period = 100, callback = checkButtons)
