import tkinter as tk
import tkinter.ttk as ttk

class CanvasApp:
   def __init__(self, parentWindow):
      self.window = parentWindow
      self.canv = tk.Canvas(self.window, width=300, height=300)
      self.canv.grid(row=0, column=0)
      
      self.canv.create_rectangle(10,10,290,290, fill='green')
      self.canv.create_oval(20,20,280,280, fill='yellow')

window = tk.Tk()
app = CanvasApp(window)
window.mainloop()
