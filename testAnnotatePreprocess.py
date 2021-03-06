#!/usr/bin/env python
import os
import errno
import glob

'''
This file will act as a python module for parsing Training Data in appropriate .col format in our experiments
'''

#Parse Path of directory into. col format
def parseTimeML(Path):
        os.system('python convertTimeMLToColumns.py '+Path+' -p stanford -o data/te3-platinum-col')
      
#Select Relevant Columns for input
def inputCol():
    #For each line in file
    input = ""
    #Training Directory is here
    allFiles = glob.glob("data/te3-platinum-col/*.col")
    
    #Read Files one by one
    for colFile in allFiles:
        
        colFile_name = nameFile(colFile)

        #do processing for single file
        with open(colFile) as f:
            next(f)
            input = ""
            for line in f:
                #Split columns on tab values
                columns = line.split("\t")
                
                #Split if columns are present
                if len(columns) >= 2:
                    #Add to input word, events and time-exps
                    if columns[0] == "2 1/2":
                        columns[0] = str(2.5)
                    input = input + columns[0] + "\t"+parseEntity(columns[3],  columns[11]) +"\n"
                    
            #Write input to a file
            filename = 'stanford-ner-2015-12-09/data/te3-platinum-col'+ colFile_name
            
            #Create Directory Structure (if does not exist) and write input Colfile to it
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
                    
            #write output to file            
            with open(filename, "w") as file:
                file.write(input)
                file.write(input)
                file.close()
    
#parse Tag in apporpriate format
def parseEntity(event,  time):
    if event[0]=="e":
        c = "EVENT"
    elif time[0]=="t":
        c = "TIMEX3"
    else:
        c = "OTHERS"
    return c
    
#return name of the file   
def nameFile(file):
    file_name = file.split("/")
    return file_name[2]



