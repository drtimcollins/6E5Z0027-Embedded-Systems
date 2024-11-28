import tkinter as tk
import tkinter.ttk as ttk

class HeaterApp:
    def __init__(self, parentWindow):
        self.window = parentWindow
        self.actualTempLabel = ttk.Label(self.window, text="Actual Temperature [C]:")
        self.boilerOnLabel = ttk.Label(self.window, text="Boiler state:")
        self.targetTempLabel = ttk.Label(self.window, text="Target Temperature [C]:")        
        self.actualTemp = ttk.Label(self.window)
        self.targetTemp = ttk.Entry(self.window)
        self.targetTemp.bind('<Key-Return>', self.targetCallback)
        self.boilerOn = ttk.Label(self.window)
        #self.btn = ttk.Button(window, text='Enter', command=self.buttonCallback)
        
        self.isEnabled = ttk.Checkbutton(self.window, text="Heating Enabled", 
                                         command=self.enableCallback)
        self.isEnabled.invoke()                     # Set initial state to 'selected'
        
        self.actualTempLabel.grid(column = 0, row = 0, sticky='e')
        self.actualTemp.grid(column = 1, row = 0, sticky='w')
        self.boilerOnLabel.grid(column = 0, row = 1, sticky='e')
        self.boilerOn.grid(column = 1, row = 1, sticky='w')
        self.targetTempLabel.grid(column = 0, row = 2, sticky='e')
        self.targetTemp.grid(column = 1, row = 2, sticky='w')
        self.isEnabled.grid(column = 0, row = 3)

    def enableCallback(self):
        print("Checked.")
        print('selected' in self.isEnabled.state())
    def targetCallback(self, event):
        print(self.targetTemp.get())
#   def buttonCallback(self):
#      print("Text entered is: " + self.txt.get())

window = tk.Tk()
app = HeaterApp(window)
window.mainloop()
