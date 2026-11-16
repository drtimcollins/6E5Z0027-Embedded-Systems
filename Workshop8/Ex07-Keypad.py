from machine import Pin, Timer
import time
time.sleep(0.1)

# Rows are connected as inputs with an internal pull-up resistor.
rowPins = (Pin(15, Pin.IN, Pin.PULL_UP), Pin(14, Pin.IN, Pin.PULL_UP), 
            Pin(13, Pin.IN, Pin.PULL_UP), Pin(12, Pin.IN, Pin.PULL_UP))
# Columns are Open Drain outputs: grounded when low, open circuit when high.
colPins = (Pin(11, Pin.OPEN_DRAIN), Pin(10, Pin.OPEN_DRAIN),
            Pin(9, Pin.OPEN_DRAIN), Pin(8, Pin.OPEN_DRAIN))
# Lookup table for the meaning of each key.
keyValues = ("123A","456B","789C","*0#D")
# Storage for the state of each key. Used to detect changes in button presses.
keyStates = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

def scanKeys(timer):  
    for col in range(4):                                      # Scan through all 4 columns
        colPins[col].value(0)                                 # Connects the column to GND
        for row in range(4):                                  # Scan through all 4 rows
            if rowPins[row].value() != keyStates[row][col]:   # Only looking for changes
                keyStates[row][col] = rowPins[row].value()    # Store new key state
                if keyStates[row][col] == 0:                  # Respond if new state is 0,
                   print(keyValues[row][col], end="")         # i.e. connected to GND.
        colPins[col].value(1)                                 # Set column to 'floating'

tmr = Timer(freq = 100, callback=scanKeys)
