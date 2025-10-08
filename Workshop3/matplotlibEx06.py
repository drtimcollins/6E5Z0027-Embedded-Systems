import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()                       # Called so we can set labels later

w = np.logspace(-2,2,200)                     # Log array between 0.01 and 100
s = 1j * w                                    # Calculate s = jw
H_dB = 20*np.log10(np.abs(s/(4*s**2+s+4)))    # Calculate H and convert to dB
ax.semilogx(w, H_dB)                          # Log x axis, linear y axis

ax.set_xlabel('Frequency [rad/s]')
ax.set_ylabel('Magnitude Response [dB]')
plt.show()
