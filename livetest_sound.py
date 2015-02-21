#Import libraries
import cv2
import cPickle
import numpy as np
#for audio output
import pyttsx
#start Video capture
cap = cv2.VideoCapture(0)

'''
Trainer File
'''
#initialize audio engine
engine = pyttsx.init()
#initialize an empty image to check for all contour position throughout
last=np.zeros((480,640,1),np.uint8)
cv2.line(last,(210,0),(210,480),(255,255,255))
cv2.line(last,(420,0),(420,480),(255,255,255))
cv2.line(last,(0,160),(640,160),(255,255,255))
cv2.line(last,(0,320),(640,320),(255,255,255))

#Open file for moments
fmina = open("minm.txt","r")
fmaxa = open("maxm.txt","r")
#Extract the training sets to two list mina and maxa
mina = fmina.read().split(" ")
maxa = fmaxa.read().split(" ")
#close the connections
fmina.close()
fmaxa.close()
#Open file for histograms
fmina = open("minh.txt","r")
fmaxa = open("maxh.txt","r")
#Extract the training sets to two list mina and maxa
minh = fmina.read().split(" ")
maxh = fmaxa.read().split(" ")
#Find the largest contour
count=0
finaltl=[]
finalbr=[]
while True:
    
    top_left = (0,0)
    bottom_right = (0,0)
    ret,im = cap.read()
    img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    (thresh,imgg)=cv2.threshold(img,10,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    ret,thresh = cv2.threshold(img,127,255,0)
    hierarchy,contours,DUMMY = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    tmp = cPickle.dumps(contours)
    contours = cPickle.loads(tmp)
    
    areas=[]
    areatmp=[]
    
    for c in contours:
        area = cv2.contourArea(c, False)
        areas.append(area)
        areatmp.append(area)
    areas.sort()
    areas.reverse()
    try:
        ind = areatmp.index(areas[1])
        ctrs = contours[ind]
    except IndexError:
        pass
    
    img1=np.zeros((480,640,1),np.uint8)

    cv2.drawContours(img1,ctrs,-1,(255,255,255),3)

    flat = ctrs.flatten()
    ptsx=[]
    ptsy=[]
    for i in range(0,len(flat),2):
        ptsx.append(flat[i])
        ptsy.append(flat[i+1])
    top_left = (min(ptsx),min(ptsy))
    bottom_right = (max(ptsx),max(ptsy))
#Till here we have identified the bounding box for the object of interest
#Calculate histogram values for the bounded box
    mask=np.zeros((bottom_right[1]-top_left[1]+1,bottom_right[0]-top_left[0]+1,1),np.uint8)
    for i in range(top_left[1],bottom_right[1]+1):
        for j in range(top_left[0],bottom_right[0]+1):
            mask[i-top_left[1]][j-top_left[0]] = img[i][j]
    vals=mask.mean(axis=2).flatten()
    counts,bins=np.histogram(vals,range(257))
    #plot histograms between 0...255
    sumh=counts[0]
    g=0
    arr=[]
    for i in range(1,256):
        if i%8!=0:
            sumh+=counts[i]
            counts[i]=0
        else:
            t=counts[i]
            counts[i]=sumh
            arr.append(sumh)
            sumh=t
    #Calculate moments for the bounded box
    mat = np.zeros((bottom_right[1]-top_left[1]+1,bottom_right[0]-top_left[0]+1,1),np.uint8)
##    cv2.rectangle(img1,top_left,bottom_right,(127,127,127))
##    cv2.rectangle(im,top_left,bottom_right,(127,127,127))
    for i in range(top_left[1],bottom_right[1]+1):
        for j in range(top_left[0],bottom_right[0]+1):
            mat[i-top_left[1]][j-top_left[0]] = img[i][j]



    moms=[]
    moms = cv2.HuMoments(cv2.moments(mat)).flatten()
    sum1=0
    sum2=0
 #   print arr
    for i in range(7):
        sum1 += (moms[i]-np.float64(mina[i]))*(np.float64(maxa[i])-moms[i])
    for i in range(31):
        sum2 += (arr[i]-int(np.float64(minh[i])))*int((np.float64(maxh[i]))-arr[i])
 #   print sum1
 #   print sum2
    if sum1>0 and sum2>0:
        #print top_left,bottom_right
        y=(bottom_right[0]+top_left[0])/2
        x=(bottom_right[1]+top_left[1])/2
        yt=(x/160)
        xt=(y/210)

        engine.say(["bottom","C","Top"][yt])
        engine.say(["Right","C","Left"][xt])
##
##        if xt==1 and yt==1 # counter pending:
##        """
##            GOES TO NEXT STAGE
##        """
##            function()
            
        
        sum1=0
        sum2=0
        #cv2.rectangle(img,top_left,bottom_right,(127,127,127))
        cv2.rectangle(im,top_left,bottom_right,(127,127,127))
        last[x][y]=255
        #cv2.rectangle(last,top_left,bottom_right,(255,255,255))
    else:
        engine.say("No")
    engine.runAndWait()
    cv2.imshow("EXE",im)
    cv2.imshow("Recctangles",last)


    if cv2.waitKey(100)==27:
        cv2.destroyAllWindows()
        
        break
