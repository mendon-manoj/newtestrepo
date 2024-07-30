import cv2
import imagehash
import numpy as np
from PIL import Image

# read images
image1 = cv2.imread("D:\drishti\data1.jpg")
image2 = cv2.imread("D:\drishti\data2.jpg")

 # convert to grayscale
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

im_pil1 = Image.fromarray(image1)
image1_hash = imagehash.dhash(im_pil1)

im_pil2 = Image.fromarray(image2)
image2_hash = imagehash.dhash(im_pil2)

# compute hamming distance
distance = image1_hash - image2_hash

print(distance)
