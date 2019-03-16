#CCC2018 J4

N=int(input())

graph=[]
for i in range (0,N):
    graph+=[input().split(" ")]

"""
N=2
graph =[[9, 2],[3, 1]]
"""
def determineAngle(graph):
    x1=int(graph[0][0])
    x2=int(graph[0][1])
    y1=x1
    y2=int(graph[1][0])
    if x1 > x2:
        if y1 < y2:
            return 90
        else:
            return 180
    else:
        if y1 < y2:
            return 360
        else:
            return 270

angle=determineAngle(graph)
newGraph=[]
if angle==90:
    for i in range (0,N):
        row=[]
        for j in range (0,N):
            row+=[graph[j][len(graph[j])-i-1]]
        newGraph+=[row]

if angle==360:
    newGraph=graph

if angle==180:
    for i in range (0,N):
        row=[]
        for j in range (0,N):
            row+=[graph[len(graph)-i-1][len(graph[j])-j-1]]
        newGraph+=[row]

if angle==270:
    for i in range (0,N):
        row=[]
        for j in range (0,N):
            row+=[graph[len(graph)-j-1][i]]
        newGraph+=[row]

def printNewGraph():
    for row in newGraph:
        line=""
        for number in row:
            line+=str(number)+" "
        print(line[:len(line)-1])

printNewGraph()
