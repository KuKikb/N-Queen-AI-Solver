##THIS IS THE MAIN FILE WHICH HAS TO BE RUN

from re import M
import cv2
import numpy as np
from util import *
from copy import deepcopy
from nQ_algo import NQ
from hopeagain import *


imgStandard = 100
#path = r"D:\PROJECTS\submat1.jpg"
path = r"C:\Users\KUKI\Desktop\blankMatrix.jpg"
#path = r"C:\Users\KUKI\Desktop\Screenshot 2022-05-19 174122.jpg"
image,originalShape = Crop(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find number of rows 
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts = cv2.findContours(horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
rows = 0
for c in cnts:   
    rows += 1
    
print('Rows:', rows - 1)
print('Columns:', rows - 1)

image = cv2.resize(image, (imgStandard*(rows-1),imgStandard*(rows-1)))

temp_image = deepcopy(image)

boxes = split_boxes(temp_image,rows-1)
print(len(boxes))

#N-Queen solutions

N_Object = NQ(rows-1)
N_Object.Nqueens(1)


#Put text on Image
for n in range(len(N_Object.solutions)):

    print(N_Object.solutions[n])
    for i in range (1,len(N_Object.solutions[n])):
        M = (i-1)+(rows-1)*(N_Object.solutions[n][i]-1)
        cv2.putText(boxes[M], 'Q', (40,70), cv2.FONT_HERSHEY_SIMPLEX, 
                    1.5, (255, 0, 0), 2, cv2.LINE_AA)

    temp = cv2.resize(temp_image, (700,700))
    cv2.imshow('sol', temp)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    choice = input("Another Solution(y/n): ")
    if n == len(N_Object.solutions)-1:
        print("last possible solution")
    elif choice == "n":
        break
    else:
        temp_image = deepcopy(image)
        boxes = split_boxes(temp_image,rows-1)
        continue
        
    