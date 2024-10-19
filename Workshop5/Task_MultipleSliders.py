import tkinter as tk
import tkinter.ttk as ttk

class SliderApp:
   def __init__(self, parentWindow):
      self.window = parentWindow
      
      self.canv = tk.Canvas(self.window, width=300, height=300, bg='white')
      self.labelX = ttk.Label(self.window, text="X:")
      self.labelY = ttk.Label(self.window, text="Y:")
      self.sliderX = ttk.Scale(self.window, command = self.setX)
      self.sliderY = ttk.Scale(self.window, command = self.setY)

      self.canv.grid()
      self.labelX.grid()
      self.labelY.grid()
      self.sliderX.grid()
      self.sliderY.grid()
      
      self.x = 0
      self.y = 0
      self.shape = self.canv.create_rectangle(0,0,20,20, fill='red')      

   def setX(self, value):
      self.x = 280*float(value)
      self.canv.moveto(self.shape, self.x, self.y)
   def setY(self, value):
      self.y = 280*float(value)
      self.canv.moveto(self.shape, self.x, self.y)
      
window = tk.Tk()
app = SliderApp(window)
window.mainloop()
