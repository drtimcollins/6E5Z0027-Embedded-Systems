import json

# Create the dataset to be output
bom = [{"Item":"Resistor", "Value":1000, "Quantity":2},
       {"Item":"Sheet", "Material":"Steel", "Dimensions":{"Length":300, "Width":100}},
       {"Item":"Adhesive", "Type":"PVA", "Volume":20}]

with open('bom.json','w') as outputFile:      # Create and open the output file
   outputFile.write(json.dumps(bom))          # Convert to json format and write to file
