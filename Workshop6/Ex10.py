from machine import UART, Pin, Timer

uart = UART(0, baudrate=1000, tx=Pin('GP0'), rx=Pin('GP1'))
btn1 = Pin('GP17', Pin.IN)             # Set up input pins for buttons 1 & 2
btn2 = Pin('GP16', Pin.IN)

def sendByte(timer):
   if btn1.value() and btn2.value():
      uart.write('?f')        # Transmit '?':0b00111111, 'f':0b01100110
   elif btn1.value():
      uart.write('?~')        # Transmit '?':0b00111111, '~':0b01111110
   elif btn2.value():
      uart.write('~?')        # Transmit '~':0b01111110, '?':0b00111111
   else:
      uart.write('??')        # Transmit '?':0b00111111, '?':0b00111111

# Set up a timer to trigger every 50 ms
tmr = Timer(period = 50, callback = sendByte)