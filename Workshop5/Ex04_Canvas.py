import tkinter as tk
import tkinter.ttk as ttk

class CanvasApp:
   def __init__(self, parentWindow):
      self.window = parentWindow
      # Create Canvas widget with set size and place in window
      self.canv = tk.Canvas(self.window, width=300, height=300)
      self.canv.grid()
      
      self.canv.create_rectangle(10,10,290,290, fill='green')   # Big green square
      self.canv.create_oval(20,20,280,280, fill='yellow')       # Smaller yellow circle

window = tk.Tk()
app = CanvasApp(window)
window.mainloop()
