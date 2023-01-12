import cv2
import numpy as np
from util import *

#FUNCTION TO CROP OUT THE MATRIX FROM THE IMAGE

def Crop(path):

        file =  path
        im1 = cv2.imread(file, 0)
        im = cv2.imread(file)
        imgHeight = im.shape[0]
        imgWidth = im.shape[1]

        ret,thresh_value = cv2.threshold(im1,180,255,cv2.THRESH_BINARY_INV)

        kernel = np.ones((5,5),np.uint8)
        dilated_value = cv2.dilate(thresh_value,kernel,iterations = 1)

        contours, hierarchy = cv2.findContours(dilated_value,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        biggest = biggestContour(contours)
        print(biggest)
        if biggest is not None:
                biggest = reorder(biggest) 
                pts1 = np.float32(biggest)
                pts2 = np.float32([[0,0],[imgWidth,0],[0,imgHeight],[imgWidth,imgHeight]])
                matrix = cv2.getPerspectiveTransform(pts1,pts2)
                imgWarpColored = cv2.warpPerspective(im,matrix,(imgWidth,imgHeight))

        return imgWarpColored,imgWarpColored.shape