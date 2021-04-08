import cv2 
import numpy as np 
import os

def write_image_contours(f):

    root = '../Images/Originals'
    dst = '../Images/Contours'
    dst_size = (100,100)

    image = cv2.imread(os.path.join(root,f)) 
    image = cv2.resize(image, dst_size, interpolation=cv2.INTER_AREA)
    final_image = np.zeros(image.shape)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    _, edged = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

    longest_contour = 0
    chosen_contour = 0

    cv2.drawContours(final_image, contours, -1, (255, 255, 255), 1) 

    cv2.imwrite(os.path.join(dst, f), final_image)
    cv2.destroyAllWindows()