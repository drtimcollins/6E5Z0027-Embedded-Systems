import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

window = tk.Tk()
window.title('Matplotlib and Tkinter Demo')

fig = Figure()
phi = np.linspace(0, 2 * np.pi)
ax = fig.subplots()
ax.plot(phi, np.sin(phi))
ax.set_xlabel('angle [rad]')
ax.set_ylabel('sin(angle)')

canv = FigureCanvasTkAgg(fig, master=window)
canv.draw()

canv.get_tk_widget().grid()

window.mainloop()
