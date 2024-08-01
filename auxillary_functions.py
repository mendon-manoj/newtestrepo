#code to read command line argument in python
import sys
print ('argument list', sys.argv)
name = sys.argv[1]
print ("Hello {}. How are you?".format(name))

# command to to execute e.g. python test.py manoj
#------------------------------------------------------------------------
#code to read files from directory
import os 
  
# Folder Path 
path = "C:/Users/C60091/Pictures"

with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name)

#------------------------------------------------------------------------
#code to slice video into images
import cv2
print('test')
capture = cv2.VideoCapture('D:/drishti/KTSession1.mp4')
print('test1')
framenr = 0

while (True):
    success, frame = capture.read()
    if success:
        cv2.imwrite(f'D:/drishti/output/frame_{framenr}.jpg', frame)
    else:
        break
    framenr += 1
    print(framenr)    

capture.release()

#------------------------------------------------------------------------
