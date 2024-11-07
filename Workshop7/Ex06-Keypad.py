from machine import Pin, Timer

rowPins = (Pin(26, Pin.IN, Pin.PULL_UP), Pin(22, Pin.IN, Pin.PULL_UP), 
            Pin(21, Pin.IN, Pin.PULL_UP), Pin(20, Pin.IN, Pin.PULL_UP))
colPins = (Pin(19, Pin.OPEN_DRAIN), Pin(18, Pin.OPEN_DRAIN),
            Pin(17, Pin.OPEN_DRAIN), Pin(16, Pin.OPEN_DRAIN))
keyValues = ("123A","456B","789C","*0#D")

def scanKeys():    
    for col in range(4):
        colPins[col].value(0)
        for row in range(4):
            if rowPins[row].value() == 0:
                colPins[col].value(1)
                return keyValues[row][col]
        colPins[col].value(1)
    return ""

lastKey = ""
def updateKeys(timer):
    global lastKey
    newKey = scanKeys()
    if lastKey != newKey:
        lastKey = newKey
        if len(lastKey) > 0:
            print(lastKey,end="")

tmr = Timer(freq = 100, callback=updateKeys)