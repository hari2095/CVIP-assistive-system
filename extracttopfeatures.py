import numpy
f=open("topfeatures.txt","r")
##g=open("histogram_ideal.txt","r")
#Calculate the min and max value for moments
moms=f.read().split(" ")
##hist=g.read().split(" ")
minm=[]
maxm=[]

if moms[-1]=="":
    moms.remove("")
for i in range(7):
    minm.append(min(numpy.float64(moms[i::7])))
    maxm.append(max(numpy.float64(moms[i::7])))

mfile=open("mintop.txt","w")
Mfile=open("maxtop.txt","w")
for m in minm:
    mfile.write(str(m)+" ")



for m in maxm:
    Mfile.write(str(m)+" ")

mfile.close()
Mfile.close()
#calculate the min and max for histograms

##minh=[]
##maxh=[]
##if hist[-1]=="":
##    hist.remove("")
##
##
##for i in range(32):
##    a=[]
##    a=hist[i::32]
##    a.sort()
##    minh.append(int(a[6]))
##    maxh.append(max(numpy.int64(hist[i::32])))
##print minh
##print maxh
##mfile=open("minh.txt","w")
##for m in minh:
##    mfile.write(str(m)+" ")
##mfile.close()
##
##Mfile=open("maxh.txt","w")
##for m in maxh:
##    Mfile.write(str(m)+" ")
##Mfile.close()
  
