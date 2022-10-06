#A simple program to polish DSF output by deleting every second column. 
#A tidy output file should appear on your desktop as 'Clean Output.txt'.
#Please DELETE the 'Clean Output.txt' after each use or else it'll just keep adding new data each time you run this program.

#Made by Andy Tuckey, October 2022.
#Don't judge my code Adrian!

#Change the input file here:
inputfile = "Desktop/20221005 OsD14 DSF.txt"

import csv

with open(inputfile, newline='\n') as f: #Opens the input file
    reader = csv.reader(f, delimiter = "\t") 
    outputfile = open("Desktop/Clean Output.txt", "a") #creates the output file
    counter = 0
    for d in list(reader): #'d' represents a row
        if len(d) != 0: #To stop the program crashing at the end of the document lol
            outputfile.write(d[0]+",") #Maintains one temperature column of the left hand side of the document
        for x in d: #'x' represents a column within row 'd' (a single value)
            if counter == 0: #ignores the temperature columns
                counter = 1
            else: #writes the value to the new file
                outputfile.write(x+",")
                counter = 0
        outputfile.write("\n") #A fresh line in the new file for each new row.

f.close()
outputfile.close()
