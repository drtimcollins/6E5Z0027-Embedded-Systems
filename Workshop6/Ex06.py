from machine import ADC, Pin, Timer

adc = ADC('GP26')                        # Create ADC input object

def readAnalogueInput(timer):            # Callback function
   a_in = adc.read_u16()                 # Read ADC as an unsigned 16-bit number
   print(a_in)

# Set up a timer to trigger 4 times per second
tmr = Timer(freq = 4, callback = readAnalogueInput)