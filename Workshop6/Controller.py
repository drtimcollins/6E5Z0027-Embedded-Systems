from machine import ADC, Timer, PWM, Pin

led = Pin('GP19', Pin.OUT)                  # Create input and output Pin objects
btn = Pin('GP17', Pin.IN)
adc = ADC('GP26')                           # Create ADC input object
pwm = PWM('GP18', freq=1000)                # create a PWM object

def callbackFunction(timer):
   a_in = adc.read_u16()
   # To do: Complete this function to add required functionality.

# Set up a timer to trigger 20 times per second
tmr = Timer(freq = 20, callback = callbackFunction)
