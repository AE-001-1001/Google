import cv2
import numpy as np

def create_mask(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([12, 25, 25])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    # another mask for red

    lower_red = np.array([0, 25, 25])
    upper_red = np.array([12, 255, 255])
    lower_gray = np.array([0, 0, 0])
    upper_gray = np.array([255, 25, 25])
    lower_blue = np.array([100, 25, 25])
    upper_blue = np.array([255, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    created_mask = mask + mask_red + mask_gray + mask_blue
    
    return created_mask

def Random_Background(image):
    # Sets the cvtColor to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Sets the image to a random background
    image = cv2.addWeighted(image, 4, cv2.GaussianBlur(image, (0, 0), 30), -4, 128)
    # Sets the cvtColor to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # use the mask to remove the background
    mask = create_mask(image)
    image = cv2.bitwise_and(image, image, mask=mask)
    return image


def run():
    SelectedIMG = cv2.imread('../../pictures/16.png')
    # resize the images to auto-scale
    SelectedIMG = cv2.resize(SelectedIMG, (0, 0), fx=0.5, fy=0.5)

    # use the function to create a mask
    #mask = create_mask(SelectedIMG)
    randomBack = Random_Background(SelectedIMG)
    # apply the mask to the image
    masked_image = cv2.bitwise_not(SelectedIMG, randomBack)
    cv2.imshow('masked image', masked_image)
    # wait for a key to be pressed
    cv2.waitKey(0)
    return 0


if __name__ == '__main__':
    run()
