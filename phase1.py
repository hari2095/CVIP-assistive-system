import cv2
import numpy as np

#### Initializing Camera ####
cap=cv2.VideoCapture(0)


#### Reading files ####
fmin = open("minm.txt","r")
fmax = open("maxm.txt","r")

minm = fmin.read().split(" ")
maxm = fmax.read().split(" ")

#### Preparing lists ####

minm.remove("")
maxm.remove("")
for i in range(7):
    minm[i] = np.float64(minm[i])
    maxm[i] = np.float64(maxm[i])


#### Frame comparison ####
ctr = 0


def look_for_object(img):
    down = 0
    up = 0
    left = 0
    right = 0
    topleft = 0
    topright = 0
    btmleft = 0
    btmright = 0
    for i in range(240,480):
        if img[i][320]<40:
            down += 1
    if down>80:
        print "Look Down"
        return

    for i in range(240):
        if img[i][320]<40:
            up += 1
    if up>80:
        print "Look Up"
        return

    for j in range(320,640):
        if img[240][j]<40:
            right += 1
    if right>80:
        print "Look Right"
        return

    for j in range(320):
        if img[240][j]<40:
            left += 1
    if left>80:
        print "Look Left"
        return

    i = 240
    j = 320
    while (i<450 or j<600):
        if img[i][j]<40:
            btmright+=1
        i+=1
        j+=1
        if i==475:
            break
        if j==620:
            break
    if btmright>75:
        print "Go Bottom Right"
        return
        
    i = 240
    j = 320
    while True:
        if img[i][j]<40:
            topleft+=1
        i-=1
        j-=1
        if i==10:
            break
        if j==20:
            break
    if topleft>75:
        print "Go Top Left"
        return

    i = 240
    j = 320
    while True:
        if img[i][j]<40:
            topright+=1
        i-=1
        j+=1
        if i==10:
            break
        if j==600:
            break
    if topright>75:
        print "Go Top Right"
        return

    i = 240
    j = 320
    while True:
        if img[i][j]<40:
            btmleft+=1
        i+=1
        j-=1
        if i==420:
            break
        if j==20:
            break
    if btmleft>75:
        print "Go Bottom Left"
        return









    
while True:
    ret,im=cap.read()
##    img=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    cv2.rectangle(im,(240,140),(400,340),(255,255,255))
    cv2.imshow("Show",im)
    mat = np.zeros((200,160,3),np.uint8)    
    for i in range(141,341):
        for j in range(241,401):
            mat[i-141][j-241]=im[i][j]
    mat = cv2.cvtColor(mat,cv2.COLOR_BGR2GRAY)
    moms = cv2.HuMoments(cv2.moments(mat)).flatten()
    summ = 0
    for i in range(7):
        summ += (moms[i]-np.float64(minm[i]))*(np.float64(maxm[i])-moms[i])
    if summ>0:
        print "Match"
        ctr += 1
        if ctr==10:
            print "OBJECT FOUND"
            cv2.destroyAllWindows()
            break
    else:
        ctr = 0
        look_for_object(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY))

    if cv2.waitKey(20)==27:
        cv2.destroyAllWindows()
        break
    
