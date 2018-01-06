#rockVmineContents.py
__author__='mike_bowles'
import urllib.request
import sys

target_url=("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data=urllib.request.urlopen(target_url)

xList=[]
labels=[]

comma=','  #in python3, treat string differently.
for line in data:
    row=line.strip().split(str.encode(comma)) #encoding is neccesary
    xList.append(row)
    
nrow=len(xList)
ncol=len(xList[1])

type=[0]*3
colCounts=[]

for col in range(ncol):
    for row in xList:
        try:
            a=float(row[col])
            if isinstance(a,float):
                type[0]+=1
        except ValueError:
            if len(row[col])>0:
                type[1]+=1
            else:
                type[2]+=1

    colCounts.append(type)
    type=[0]*3
    
print("Col#"+'\t\t'+"Number"+'\t\t'+"Strings"+'\t\t'+"Other\n")
iCol=0
for  types in colCounts:
    print(str(iCol)+'\t\t'+str(types[0])+'\t\t'+str(types[1])+'\t\t'+str(types[2])+"\n")
    iCol+=1

