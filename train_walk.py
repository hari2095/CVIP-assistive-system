'''

TRAIN FOR IDENTIFYING AFTER HAVING WALKED AHEAD

'''

import cv2
import numpy as np

f = open("topfeatures.txt","a")
cap = cv2.VideoCapture(0)

while True:
    ret,im = cap.read()
    cv2.rectangle(im,(120,340),(520,460),(255,0,0))
    mat = np.zeros((120,400,3),np.uint8)    
    if cv2.waitKey(40) == 99:
    
        for i in range(341,460):
            for j in range(121,521):
                mat[i-341][j-121]=im[i][j]
        cv2.rectangle(im,(120,340),(520,460),(0,0,255))
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

  
