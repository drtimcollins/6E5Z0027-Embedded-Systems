import csv

items = []                        # Empty list to begin with
with open('bom.csv','r') as inputFile:
   reader = csv.reader(inputFile)
   columns = next(reader)
   for row in reader:
      items.append(row)

print(columns)                     # Shows the column headings
print(items)                       # The original bom data
