#rockVmineSummaries.py
__author__='mike_bowles'
import urllib.request
import sys

target_url=("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data=urllib.request.urlopen(target_url)

xlist=[]
labels=[]

#in python3, treat string differently.
#encoding is neccesary
comma=','
for line in data:
    row=line.strip().split(str.encode(comma))
    xlist.append(row)

#did not write to a .txt; print the result instead
print("number of rows of data="+str(len(xlist))+'\n')
print("number of columns of data="+str(len(xlist[1]))+'\n')

