import tkinter as tk
import tkinter.ttk as ttk

class ButtonTextApp:
   def __init__(self, parentWindow):
      self.window = parentWindow
      self.txt = ttk.Entry(self.window)
      self.btn = ttk.Button(self.window, text='Enter', command=self.buttonCallback)
      self.txt.grid(column = 0, row = 0, sticky='e')    # 'sticks' to the East (right)
      self.btn.grid(column = 1, row = 0, sticky='w')    # 'sticks' to the West (left)

      self.window.columnconfigure(0, weight = 1)   # Set all rows and columns with weight=1
      self.window.columnconfigure(1, weight = 1)   # They will all grow at the same rate
      self.window.rowconfigure(0, weight = 1)      # when the window is resized.

   def buttonCallback(self):
      print("Text entered is: " + self.txt.get())

window = tk.Tk()
app = ButtonTextApp(window)
window.mainloop()
