import numpy
f=open("data.txt","r")
moms=f.read().split(" ")
minm=[]
maxm=[]
if moms[-1]=="":
    moms.remove("")
for i in range(7):
    minm.append(min(numpy.float64(moms[i::7])))
    maxm.append(max(numpy.float64(moms[i::7])))

mfile=open("mint.txt","w")
for m in minm:
    mfile.write(str(m)+" ")
mfile.close()

Mfile=open("maxt.txt","w")
for m in maxm:
    Mfile.write(str(m)+" ")
Mfile.close()
