import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
phi = np.pi * x / 50
fig, axs = plt.subplots(2,1)    # Create a 2x1 grid of subplot Axes objects
axs[0].plot(phi, np.sin(phi))   # Plot the sine wave to Axes object 0 (top)
axs[1].plot(phi, np.cos(phi))   # Plot the cosine wave to Axes object 1 (bottom)
plt.show()
