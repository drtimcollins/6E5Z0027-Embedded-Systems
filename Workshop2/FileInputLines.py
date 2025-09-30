with open('testfile.txt','r') as inputFile:
   for line in inputFile:                   # Iterate through each line of the file
      line = line.rstrip()                  # Remove non-printing chars from end of string
      print(line)                           # and print the result
