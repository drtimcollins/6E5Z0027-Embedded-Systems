from machine import ADC, Timer, PWM

adc = ADC('GP26')                           # Create ADC input object for the pot
pwm = PWM('GP19', freq=1000)                # create a PWM object for LED 1

def readAnalogueInput(timer):               # Callback function
   a_in = adc.read_u16()                    # Read ADC as an unsigned 16-bit number.
   pwm.duty_u16(a_in)                       # Set duty to the ADC input value
   print(a_in)                              # and print to the Shell for reference.

# Set up a timer to trigger 4 times per second
tmr = Timer(freq = 4, callback = readAnalogueInput)