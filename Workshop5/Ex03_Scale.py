import tkinter as tk
import tkinter.ttk as ttk

class ScaleApp:
   def __init__(self, parentWindow):
      self.window = parentWindow
      
      self.slider = ttk.Scale(window, command=self.sliderCallback)
      self.txt = ttk.Label(window, background='#000000', width=10)
      
      self.slider.grid(column = 0, row = 0)
      self.txt.grid(column = 1, row = 0)

   def sliderCallback(self, value):
      c = round(float(value)*255)
      self.txt.config(background = f'#{c:02x}{c:02x}{c:02x}')

window = tk.Tk()
app = ScaleApp(window)
window.mainloop()
