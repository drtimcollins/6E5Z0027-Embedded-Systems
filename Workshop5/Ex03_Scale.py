import tkinter as tk
import tkinter.ttk as ttk

class ScaleApp:
   def __init__(self, parentWindow):
      self.window = parentWindow
      # Create a Scale widget with callback function
      self.slider = ttk.Scale(window, command=self.sliderCallback)
      # Create an empty label, just used to display a coloured box
      self.txt = ttk.Label(window, background='#000000', width=10)
      
      self.slider.grid(column = 0, row = 0)    # Place widgets using grid()
      self.txt.grid(column = 1, row = 0)

   def sliderCallback(self, value):            # value is current slider position
      c = round(float(value)*255)              # convert string to integer 0-255
      self.txt.config(background = f'#{c:02x}{c:02x}{c:02x}')   # Set colour in hex format

window = tk.Tk()
app = ScaleApp(window)
window.mainloop()
