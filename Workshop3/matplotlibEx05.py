import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()                # Called so we can set labels later

w = np.logspace(-2,2,200)              # Log array between 0.01 and 100
s = 1j * w                             # Calculate s = jw
ax.loglog(w, np.abs(s/(4*s**2+s+4)))   # loglog() uses a log x and a log y axis

ax.set_xlabel('Frequency [rad/s]')
ax.set_ylabel('Magnitude Response')
plt.show()
