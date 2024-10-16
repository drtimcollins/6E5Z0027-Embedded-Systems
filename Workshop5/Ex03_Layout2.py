import tkinter as tk
import tkinter.ttk as ttk

class ButtonTextApp:
   def __init__(self, parentWindow):
      self.window = parentWindow
      self.txt = ttk.Entry(window)
      self.btn = ttk.Button(window, text='Enter', command=self.buttonCallback)
      self.txt.grid(column = 0, row = 0, sticky='e')
      self.btn.grid(column = 1, row = 0, sticky='w')

      self.window.columnconfigure(0, weight = 1)
      self.window.columnconfigure(1, weight = 1)
      self.window.rowconfigure(0, weight = 1)

   def buttonCallback(self):
      print(self.txt.get())

window = tk.Tk()
app = ButtonTextApp(window)
window.mainloop()
