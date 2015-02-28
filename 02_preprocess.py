import glob
import cv2

pics=glob.glob("PIC*.jpg")
Feat = []
c=1
for p in pics:
    i = cv2.imread(p)
    print c
    gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    moms = cv2.HuMoments(cv2.moments(gray)).flatten()
    
    Feat.append(moms)
    c+=1

out = open("data.txt","w")
for F in Feat:
    for f in F:
        out.write(str(f)+" ")
out.close()
