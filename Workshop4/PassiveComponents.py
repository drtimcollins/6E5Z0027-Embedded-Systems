from math import pi

# The parent class: Impedance. Has a single attribute, Z, and has methods to
# implement Ohm's law and to calculate parallel and series combinations.
class Impedance:
    def __init__(self, initialImpedance):
        self.Z = initialImpedance

    def getCurrent(self, voltage):          # Calculate current given voltage
        return voltage / self.Z

    def getVoltage(self, current):          # Calculate voltage given current
        return current * self.Z

    # Create a new Impedance equal to this impedance in parallel with another, Z2
    def parallel(self, Z2):                 
        return Impedance(1.0 / (1.0/self.Z + 1.0/Z2.Z))

    # Create a new Impedance equal to this impedance in series with another, Z2
    def series(self, Z2):
        return Impedance(self.Z + Z2.Z)

# Resistor class: Inherits all the methods from Impedance except for __init__()
# which is replaced.
class Resistor(Impedance):
    def __init__(self, resistance):
        self.Z = resistance

# Capacitor class: Inherits all the methods from Impedance except for __init__()
# which is replaced with a new method that requires capacitance and frequency.
class Capacitor(Impedance):
    def __init__(self, capacitance, frequency):
        self.Z = 1/1j/2/pi/frequency/capacitance

# Inductor class: Inherits all the methods from Impedance except for __init__()
# which is replaced with a new method that requires inductance and frequency.
class Inductor(Impedance):
    def __init__(self, inductance, frequency):
        self.Z = 1j*2*pi*frequency*inductance

