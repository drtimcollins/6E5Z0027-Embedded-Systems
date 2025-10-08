import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 2*np.pi, 50)  # phi array has 50 elements from 0 to 2pi
fig, ax = plt.subplots()           # Only one plot but call this to get fig and ax
ax.plot(phi, np.sin(phi))          # Plot a single cycle of a sine wave
ax.set_xlabel('Angle')             # Set axis label and plot heading/title
ax.set_ylabel('sin(phi)')
ax.set_title('Sine Wave Example')
ax.set_xlim(0,2*np.pi)             # Set the x and y axis limits exactly
ax.set_ylim(-1,1)
ax.grid(True, color = 'green',     # Enable grid lines and make the dashed
          linestyle = '--')        # and green coloured
fig.set_figwidth(8)                # 8 inches at 100 dpi = 800 pixels wide
fig.set_figheight(4)               # 4 inches at 100 dpi = 400 pixels high
plt.show()
