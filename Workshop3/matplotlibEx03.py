import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
phi = np.pi * x / 50
fig, axs = plt.subplots(2,2)          # Two rows and two columns specified
axs[0][0].plot(phi, np.sin(phi))      # Top-left (row 0, column 0)
axs[1][0].plot(phi, np.cos(phi))      # Bottom-left (row 1, column 0)
axs[0][1].plot(phi, np.sin(2*phi))    # Top-right (row 0, column 1)
axs[1][1].plot(phi, np.cos(2*phi))    # Bottom-right (row 1, column 1)
plt.show()
