import cv2
import imagehash
from PIL import Image

img = cv2.imread("D:/Drishti/data.jpg")
img1 = cv2.imread("D:/Drishti/data.jpg")
img = cv2.resize(img, (660, 880))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imwrite("D:/Drishti/datagray.jpg", img)

grayImgWarped = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(grayImgWarped, (3, 3), 0)
cv2.imwrite("D:/Drishti/blurredImage.jpg", blurImg)

hash0 = imagehash.average_hash(blurImg)
#hash1 = imagehash.average_hash(Image.open('D:/Drishti/datagray.jpeg'))

#cutoff = 5

#hashDiff = hash0 - hash1
#print(hashDiff)
#if hashDiff < cutoff:
#    print('These images are similar!')


print("hello")
 
