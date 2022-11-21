import cv2

# load the picture
img1 = cv2.imread('../../pictures/1.png')

# change the color space to HSV
# create a mask for the color red
img3 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

cv2.imshow('image', img3)
# wait for a key to be pressed
cv2.waitKey(0)
