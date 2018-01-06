#rVMSummaryStats.py
__author__='mike_bowles'
import urllib.request
import sys
import numpy as np

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

#generate summary statistics for column3
col=3
colData=[]
for row in xList:
    colData.append(float(row[col]))
    
colArray=np.array(colData)
colMean=np.mean(colArray)
colsd=np.std(colArray)
print("Mean:"+str(colMean)+'\t\t'+"Standard Deviation:"+str(colsd)+'\n')


#calculate quantile boundaries
ntiles=4
percentBdry=[]

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray,i*100/ntiles))
print("Boundaries for %s equal percentiles" %ntiles)
print(percentBdry)


#run again with 10 intervals
ntiles=10
percentBdry=[]

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray,i*100/ntiles))
print("Boundaries for %s equal percentiles" %ntiles)
print(percentBdry)


#the last column contains categorical variables
col=60
colData=[]
for row in xList:
    colData.append(row[col])

unique=set(colData)
print("\nUnique Label Values:\t"+str(list(unique))+'\n')

catDict=dict(zip(list(unique),range(len(unique))))
catCount=[0]*2

for elt in colData:
    catCount[catDict[elt]]+=1
print(str(list(unique))+"\n")
print(catCount)



