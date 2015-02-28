import cv2
import numpy as np
import pyttsx

#### Initializing Camera ####
cap=cv2.VideoCapture(0)

#### Initialize speech engine ####
engine = pyttsx.init()


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


###################### FUNCTIONS ##############
#### GUIDANCE TO DETECT OBJECT ####
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
##        print "Look Down"
        engine.say("Look Down")
        return

    for i in range(240):
        if img[i][320]<40:
            up += 1
    if up>80:
##        print "Look Up"
        engine.say("Look Up")
        return

    for j in range(320,640):
        if img[240][j]<40:
            right += 1
    if right>80:
##        print "Look Right"
        engine.say("Look Right")
        return

    for j in range(320):
        if img[240][j]<40:
            left += 1
    if left>80:
##        print "Look Left"
        engine.say("Look Left")
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
##        print "Go Bottom Right"
        engine.say("Go Bottom Right")
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
##        print "Go Top Left"
        engine.say("Go Top Left")
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
##        print "Go Top Right"
        engine.say("Go Top Right")
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
##        print "Go Bottom Left"
        engine.say("Go Bottom Left")
        return
    engine.runAndWait()


############ BRING HAND ########

def bring_hand(frame):
##    print "PLEASE EXTEND YOUR LEFT HAND FORWARD"
    engine.say("PLEASE EXTEND YOUR LEFT HAND FORWARD")
    while True:
        ret, imh = cap.read()
        img = frame - imh
        cv2.imshow("HAND ALONE f - i",img)
        cv2.imshow("HAND ALONE i - f",-img)
        engine.runAndWait()
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break
    

###################################
    
#### Frame comparison ####
ctr = 0






def frame_or_not():
    fmin = open("mint.txt","r")
    fmax = open("maxt.txt","r")

    mins = fmin.read().split(" ")
    maxs = fmax.read().split(" ")




##    print "PLEASE READY THE CAMERA"
    engine.say("PLEASE READY THE CAMERA")
    chkr = 0
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
            chkr += 1
            print "..."
            if chkr == 10:
##                print "OBJECT FOUND"
                engine.say("OBJECT IDENTIFIED")
                calibrate()
        else:
##            print "SCANNING"
##            engine.say("SCANNING")
            chkr = 0
        engine.runAndWait()
        if cv2.waitKey(1)==27:
            cv2.destroyAllWindows()
            break    
        


def calibrate():
    ctr =0
    while True:
        ret,im=cap.read()
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
##            print "Match"
            engine.say("Match")
            ctr += 1
            if ctr==3:
##                print "OBJECT FOUND"
                engine.say("OBJECT FOUND")
                cv2.destroyAllWindows()
                frame = im
                bring_hand(frame)
                break
        else:
            ctr = 0
            look_for_object(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY))

        engine.runAndWait()
        if cv2.waitKey(1)==27:
            cv2.destroyAllWindows()
            break
    
        
frame_or_not()

