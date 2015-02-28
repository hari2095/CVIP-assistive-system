'''
ALPHA 2
'''

import cv2
import numpy as np

f = open("features.txt","a")
cap = cv2.VideoCapture(0)

while True:
    ret,im = cap.read()
    cv2.rectangle(im,(240,140),(400,340),(255,0,0))
    mat = np.zeros((200,160,3),np.uint8)    
    if cv2.waitKey(40) == 99:
    
        for i in range(141,341):
            for j in range(241,401):
                mat[i-141][j-241]=im[i][j]
        cv2.rectangle(im,(240,140),(400,340),(0,0,255))
        mat = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
        moms = cv2.HuMoments(cv2.moments(mat)).flatten()
        for i in moms:
            f.write(str(i)+" ")
    cv2.imshow("SEE",im)            
    cv2.imshow("SAW",mat)    
    if cv2.waitKey(20) == 27:
        cv2.destroyAllWindows()
        break
f.close()
