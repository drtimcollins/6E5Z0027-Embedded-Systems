import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)                # Creates a numpy array: 0, 1, 2, ..., 99
phi = np.pi * x / 50              # Scale x to range from 0 to 2.pi
plt.plot(phi, np.sin(phi))        # x is angle in radians, y is sin(x)
plt.plot(phi, np.cos(phi))        # x is angle in radians, y is cos(x)
plt.show()
