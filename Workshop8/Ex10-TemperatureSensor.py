import time
from onewire import OneWire
from ds18x20 import DS18X20
from machine import Pin, Timer
time.sleep(0.1) # Wait for USB to become ready

tempSensor = DS18X20(OneWire(Pin('GP20')))   # Setup interface using pin GP20
deviceID = tempSensor.scan()[0]  # Find device(s) - we are assuming there is only one

tempSensor.convert_temp()        # Initiate first temperature reading
time.sleep(1)                    # Conversion takes 750ms so wait 1s to make sure

def reportTemperature(tmr):
    t = tempSensor.read_temp(deviceID)       # Read temperature from device 0
    print(f'Temperature = {t}\u00b0C')
    tempSensor.convert_temp()                # Initiate the next reading

# Start timer to report temperature every 2000ms
timer = Timer(period = 2000, callback = reportTemperature)
