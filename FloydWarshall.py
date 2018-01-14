#!/usr/bin/python3
#Read file and compute All Source Shortest Path Algorithm
import sys


def getEdges():
   global node1, node2, node3;
   node1,node2,node3= line.split();

def readFileLinebyLine():
    global line
    line = file.readline()


fileNametoBeRead=sys.argv[1];
startNode=sys.argv[2];
file= open(fileNametoBeRead,"r")
graphHashMap={}
graphList=[]
readFileLinebyLine()
print(line)
getEdges()
if node1==startNode:
    graphList.append(node2)
print(node2)
counter=int(startNode);
while line:
    readFileLinebyLine()
    print(line)
    if line:
     getEdges()
     if node1==startNode:
        graphList.append(node2)
     else:
        startNode=node1
        graphHashMap[counter]=graphList
        counter +=1


graphHashMap[counter]=graphList
print(graphHashMap)

