from micropython import const
from machine import Pin
import framebuf

class DotMatrix(framebuf.FrameBuffer):           # Inherit all the bitmap drawing methods from FrameBuffer
    _DIGIT_0 = const(0x1)                        # MAX7219 Register Addresses
    _DECODE_MODE = const(0x9)
    _INTENSITY = const(0xA)
    _SCAN_LIMIT = const(0xB)
    _SHUTDOWN = const(0xC)
    _DISPLAY_TEST = const(0xF)
    
    def __init__(self, spi, cs, numDisplays, flipLR=False):
        self.spi = spi									# A machine.SPI object, mosi and sck connect to display
        self.cs = cs 									# A machine.Pin object connected to CS
        self.cs.init(Pin.OUT, value = 1)
        self.buffer = bytearray(8 * numDisplays)		# Framebuffer storage, 8 bytes per display (1 bit per pixel)
        self.N = numDisplays
        if flipLR:										# Set True for some displays wired in a mirror-image way
            super().__init__(self.buffer, 8 * numDisplays, 8, framebuf.MONO_HMSB)        
        else:
            super().__init__(self.buffer, 8 * numDisplays, 8, framebuf.MONO_HLSB)        
        self.init()

    def _sendBytes(self, buf):
        self.cs(0)
        self.spi.write(buf)
        self.cs(1)

    def init(self):
        launchSequence = ([_SHUTDOWN, 0],[_DISPLAY_TEST, 0],[_SCAN_LIMIT, 7],[_DECODE_MODE, 0],[_SHUTDOWN, 1])
        for cmd in launchSequence:
            self._sendBytes(bytes(self.N*cmd))			# Send each address/value pair N times, once for each device

    def setBrightness(self, value):
        if value < 0 or value > 15:
            raise ValueError("Brightness out of range")
        self._sendBytes(bytes(self.N*[_INTENSITY, value]))

    def show(self):
        for row in range(8):
            rowIndex = row * self.N						# Each row in the framebuffer is N bytes long
            self._sendBytes(bytes(sum(zip(self.N*[_DIGIT_0 + row], self.buffer[rowIndex:(rowIndex+self.N)]),())))


