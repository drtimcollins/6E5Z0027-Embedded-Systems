with open('testfile.txt','r') as inputFile:   # 'r' = open for reading
   text = inputFile.read()                    # Read the entire file...
   print(text)                                # ...and print to the console
   