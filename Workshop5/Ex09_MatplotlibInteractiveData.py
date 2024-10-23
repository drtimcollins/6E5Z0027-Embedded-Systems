import tkinter as tk
import tkinter.ttk as ttk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class PlotterApp():
   def __init__(self, parentWindow):
      self.window = parentWindow
      self.window.title('Matplotlib and Tkinter Demo 2')

      self.fig = Figure()                      # Same plot again
      self.ax = self.fig.subplots()
      self.phi = np.linspace(0, 2 * np.pi)
      self.plotLine = self.ax.plot(self.phi, np.sin(self.phi))
      self.ax.set_xlabel('angle [rad]')
      self.ax.set_ylabel('sin(angle)')

      self.canv = FigureCanvasTkAgg(self.fig, master=self.window)
      self.canv.draw()

      self.btn1 = ttk.Button(self.window, text='Sine', command=self.buttonCallbackSin)
      self.btn2 = ttk.Button(self.window, text='Cosine', command=self.buttonCallbackCos)
      
      self.canv.get_tk_widget().grid(row=0,column=0,columnspan=2,sticky = 'news')
      self.btn1.grid(row=1,column=0)
      self.btn2.grid(row=1,column=1)

      self.window.columnconfigure(0, weight = 1)
      self.window.columnconfigure(1, weight = 1)
      self.window.rowconfigure(0, weight = 1)
   
   def buttonCallbackSin(self):       
      self.plotLine[0].set_data(self.phi, np.sin(self.phi))  # Change the data used for
      self.ax.set_ylabel('sin(angle)')                       # the plot. In this case
      self.canv.draw()                                       # switch to a sine wave.
      
   def buttonCallbackCos(self):       
      self.plotLine[0].set_data(self.phi, np.cos(self.phi))  # Cosine wave with this
      self.ax.set_ylabel('cos(angle)')                       # button's callback.
      self.canv.draw()

window = tk.Tk()
app = PlotterApp(window)
window.mainloop()
