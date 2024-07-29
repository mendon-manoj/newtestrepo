import cv2
import imagehash
from PIL import Image

img = cv2.imread("D:/Drishti/data.jpg")
img = cv2.resize(img, (660, 880))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (3, 3), 0)

pilImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
pilImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#pilImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Get the average hashes of both images
#hash0 = imagehash.average_hash(pilImg)
#hash1 = imagehash.average_hash(Image.open('D:/Drishti/data1.jpg'))
#cutoff = 5  # Can be changed according to what works best for your images
    
#hashDiff = hash0 - hash1  # Finds the distance between the hashes of images
#if hashDiff < cutoff:
#    print('These images are similar!')
