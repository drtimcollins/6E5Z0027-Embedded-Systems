import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

window = tk.Tk()
window.title('Matplotlib and Tkinter Demo')

fig = Figure()                             # 1.  Create a Figure
ax = fig.subplots()                        # 2.  Create one or more subplots (one here)
phi = np.linspace(0, 2 * np.pi)
ax.plot(phi, np.sin(phi))                  # 3.  Create the plot (e.g. a sine wave)
ax.set_xlabel('angle [rad]')               # 3a. (optional) Add labels, titles, etc.
ax.set_ylabel('sin(angle)')

canv = FigureCanvasTkAgg(fig, master=window)   # 4. Create FigureCanvasTkAgg with fig
canv.draw()                                    # 5. Draw the plot to the canvas
canv.get_tk_widget().grid()                    # 6. Place widget in the window

window.mainloop()