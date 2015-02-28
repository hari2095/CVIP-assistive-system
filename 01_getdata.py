import cv2

N=150
cap = cv2.VideoCapture(0)
c=0
print "Please set your camera on the object to be trained."
k = raw_input("Press ENTER to begin training:")
if k=="":
    while c<N:
        ret,i1 = cap.read()
        cv2.imshow("Trainer",i1)
        if cv2.waitKey(1)==27:
            cv2.destroyAllWindows()
            break
        
        c+=1
        print c,"/",N
        cv2.imwrite("PIC"+str(c)+".jpg",i1)
