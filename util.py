import numpy as np
import cv2

def preProcess(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,
                    255,1,1,11,2)
    
    return imgThreshold

#FINDING THE OUTLINE OF THE IMAGE

def biggestContour(contours):
    biggest = np.array([])
    maxarea = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            perimeter = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02 * perimeter, True)
            if area > maxarea and len(approx) == 4:
                biggest = approx
                maxarea = area
    
    return biggest

#REORDERING THE CORNER POINTS OF THE IMAGE STORED IN THE ARGUMENT ARRAY

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2), dtype=np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew

#FUNCTION TO SINGLE OUT EACH CELL OF THE TABLE FOR USE

def split_boxes(img,n):
    rows = np.vsplit(img,n)
    boxes = []
    for r in rows:
        cols = np.hsplit(r,n)
        for box in cols:
            boxes.append(box)
            
    return boxes

    