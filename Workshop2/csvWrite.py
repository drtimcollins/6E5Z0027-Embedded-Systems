import csv                             # Import the module - don't miss this out!

items = (('Resistor', 1000, 2), ('Capacitor', 1e-6, 1))
with open('bom.csv','w', newline='') as outputFile:
   writer = csv.writer(outputFile)
   writer.writerow(('Component','Value','Quantity'))	# Write column headings
   writer.writerows(items)                              # Write bom data
