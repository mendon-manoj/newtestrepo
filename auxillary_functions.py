#code to read command line argument in python
import sys
print ('argument list', sys.argv)
name = sys.argv[1]
print ("Hello {}. How are you?".format(name))

# command to to execute e.g. python test.py manoj

#code to read files from directory
import os 
  
# Folder Path 
path = "C:/Users/C60091/Pictures"

with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name)
