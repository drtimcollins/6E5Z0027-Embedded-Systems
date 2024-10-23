import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

window = tk.Tk()
window.title('Matplotlib and Tkinter Demo')

fig = Figure()                           # Figure creation is the same as the
ax = fig.subplots()                      # previous example.
phi = np.linspace(0, 2 * np.pi)
ax.plot(phi, np.sin(phi))
ax.set_xlabel('angle [rad]')
ax.set_ylabel('sin(angle)')

canv = FigureCanvasTkAgg(fig, master=window)
canv.draw()

window.columnconfigure(0, weight = 1)          # The row and column with the figure canvas
window.rowconfigure(0, weight = 1)             # are both set to grow with the window.
canv.get_tk_widget().grid(sticky = 'news')     # Plot stick to all sides and fills
                                               # the space available.
window.mainloop()
