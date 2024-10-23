import tkinter as tk
import tkinter.ttk as ttk

class CanvasApp:
   def __init__(self, parentWindow):
      self.window = parentWindow
      # Create a Canvas, a Label and two Buttons
      self.canv = tk.Canvas(self.window, width=300, height=300)
      self.label = ttk.Label(self.window, text="Circle Colour:")
      self.btn1 = ttk.Button(self.window, width = 10, text="Red", command = self.setRed)
      self.btn2 = ttk.Button(self.window, width = 10, text="Blue", command = self.setBlue)

      # Place the widgets. Note that the Canvas widget is set to be placed in row 0,
      # column 0 and to span over three columns.
      self.canv.grid(row=0, column=0, columnspan=3)
      self.label.grid(row=1,column=0)                # Check the sketch in the workshop
      self.btn1.grid(row=1, column=1)                # notes for the desired placements.
      self.btn2.grid(row=1, column=2)
      
      self.canv.create_rectangle(10,10,290,290, fill='green')
      self.circle = self.canv.create_oval(20,20,280,280, fill='yellow')
   def setRed(self):
      self.canv.itemconfig(self.circle, fill = 'red')   # itemconfig changes the properties
   def setBlue(self):                                   # of an existing Canvas item.
      self.canv.itemconfig(self.circle, fill = 'blue')

window = tk.Tk()
app = CanvasApp(window)
window.mainloop()
