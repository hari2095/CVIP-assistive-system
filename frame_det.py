import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fmin = open("mint.txt","r")
fmax = open("maxt.txt","r")

mins = fmin.read().split(" ")
maxs = fmax.read().split(" ")




print "PLEASE READY THE CAMERA"


while True:
    ctr=0
    ret,im=cap.read()
    ig=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Eat",im)
    moms=cv2.HuMoments(cv2.moments(ig)).flatten()
    for i in range(7):
        if moms[i]>np.float64(mins[i]) and moms[i]<np.float64(maxs[i]):
            ctr+=1
    if ctr==7:
        print "OBJECT FOUND"
    else:
        print "SCANNING"
    if cv2.waitKey(1)==27:
        cv2.destroyAllWindows()
        break    
