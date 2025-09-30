import json
	
with open('bom.json','r') as inputFile:      # Open file for reading
   bom = json.loads(inputFile.read())        # Read entire file and convert from json

print(bom)                                   # Show the result
