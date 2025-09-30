with open('testfile.txt','w') as outputFile:        # Create and open file
   for i in range(1, 11):                           # Repeat from i = 1 to i = 10
      outputFile.write(f'File test line {i}.\n')    # Write a line to the file
