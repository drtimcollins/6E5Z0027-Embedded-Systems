import tkinter as tk
import tkinter.ttk as ttk
from Ex02DesktopCodeIoT import SmartHeating

class HeaterApp:
    def __init__(self, parentWindow):
        self.sh = SmartHeating()            # Create IoT interface object
        self.window = parentWindow
        self.actualTempLabel = ttk.Label(self.window, text="Actual Temperature [C]:")
        self.boilerOnLabel = ttk.Label(self.window, text="Boiler state:")
        self.targetTempLabel = ttk.Label(self.window, text="Target Temperature [C]:")        
        self.actualTemp = ttk.Label(self.window)
        self.targetTemp = ttk.Entry(self.window)
        self.targetTemp.bind('<Key-Return>', self.targetCallback)  # Called when Return hit
        self.boilerOn = ttk.Label(self.window)
        
        self.isEnabled = ttk.Checkbutton(self.window, text="Heating Enabled", 
                                         command=self.enableCallback)
        self.isEnabled.invoke()                     # Set initial state to 'selected'
        # Placement using grid() - basic, non-responsive layout
        self.actualTempLabel.grid(column = 0, row = 0, sticky='e')
        self.actualTemp.grid(column = 1, row = 0, sticky='w')
        self.boilerOnLabel.grid(column = 0, row = 1, sticky='e')
        self.boilerOn.grid(column = 1, row = 1, sticky='w')
        self.targetTempLabel.grid(column = 0, row = 2, sticky='e')
        self.targetTemp.grid(column = 1, row = 2, sticky='w')
        self.isEnabled.grid(column = 0, row = 3)
        
        self.window.after(2000, self.timerCallback)         # Called in 2000ms time
    def enableCallback(self):
        self.sh.isHeatingEnabled = ('selected' in self.isEnabled.state())
        print("Checked:",self.sh.isHeatingEnabled)
    def targetCallback(self, event):
        self.sh.targetTemperature = int(self.targetTemp.get())
        print("Target Temp:",self.sh.targetTemperature)
    def timerCallback(self):
        self.sh.postData()                                  # Update IoT data...
        self.sh.updateFromIoT()
        self.boilerOn.config(text=str(self.sh.isBoilerOn))  # ...and update GUI
        self.actualTemp.config(text=str(self.sh.actualTemperature))
        self.window.after(2000, self.timerCallback)         # Call again in 2000ms

window = tk.Tk()
app = HeaterApp(window)
window.mainloop()
