import tkinter as tk
import tkinter.ttk as ttk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class PlotterApp():
   def __init__(self, parentWindow):
      self.window = parentWindow
      self.window.title('Matplotlib and Tkinter Demo 2')

      self.fig = Figure()                           # Same figure again
      ax = self.fig.subplots()
      phi = np.linspace(0, 2 * np.pi)
      self.plotLine = ax.plot(phi, np.sin(phi))
      ax.set_xlabel('angle [rad]')
      ax.set_ylabel('sin(angle)')

      self.canv = FigureCanvasTkAgg(self.fig, master=self.window)
      self.canv.draw()
      # Add buttons with individual callback functions (defined below)
      self.btn1 = ttk.Button(self.window, text='Red', command=self.buttonCallback1)
      self.btn2 = ttk.Button(self.window, text='Green', command=self.buttonCallback2)
      # Place widgets on the grid. Buttons are placed below the plot canvas.
      self.canv.get_tk_widget().grid(row=0,column=0,columnspan=2,sticky = 'news')
      self.btn1.grid(row=1,column=0)
      self.btn2.grid(row=1,column=1)

      self.window.columnconfigure(0, weight = 1) # Set columns to grow with the window.
      self.window.columnconfigure(1, weight = 1)
      self.window.rowconfigure(0, weight = 1)    # Row 1 holds the buttons and does
                                                 # not grow.
   def buttonCallback1(self):       
      self.plotLine[0].set_color('red')          # Change line colour used in the plot.
      self.canv.draw()
      
   def buttonCallback2(self):       
      self.plotLine[0].set_color('green')
      self.canv.draw()

window = tk.Tk()
app = PlotterApp(window)
window.mainloop()
