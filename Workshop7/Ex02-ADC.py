from machine import ADC, Timer

adc = ADC('GP26')                            # Setup ADC0

def readADC(timer):
   print(f"ADC Input is: {adc.read_u16()}")  # Read and print ADC input

tmr = Timer(period=500, callback=readADC)