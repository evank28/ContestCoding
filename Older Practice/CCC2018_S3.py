#CCC2018_s3: RoboThieves -- practice on 2019-02-18
#By: Evan Kanter
from collections import deque
from textwrap import wrap

in1 = str(input())
N = int(in1[:1])
M = int(in1[1:])

grid = [wrap(input(),1) for i in range (0,N)]           #this line takes input for a grid

print(grid)   

#now we have to make the grid into a graph
graph={}
for row in grid:
        for col in grid[row]:
                value = grid[row][col]
                if value!="W":
                        graph.setdefault((row,col),{'value':value, 'neighbors':[]})
                        if (col+1<len(col)-1) and grid[row][col+1]!="W":        #checks if neighbor on right
                                graph[(row,col)]['neighbors'].append((row,col+1))
                        if  (col-1>0) and grid[row][col-1]!="W":                #checks if neighbor on left
                                graph[(row,col)]['neighbors'].append((row,col-1))
                        if  (row+1<len(row)-1) and grid[row+1][col]!="W":       #checks if neighbor above
                                graph[(row,col)]['neighbors'].append((row+1,col))
                        if  (row-1>0) and grid[row-1][col]!="W":                #checks if neighbor below
                                graph[(row,col)]['neighbors'].append((row-1,col))


#now we must use a breadth first search algorithm to determine the shortest path      


def getMinSteps (graph,start):
    """
    Iterative Breadth-First Search algorithmic method for a graph that is an adjacency list
    """
    visited = set()
    q = deque([start])

    while q:
        vertex = q.popleft()
        if vertex not in visited:
            visited.add(vertex)
            q.extend(graph[vertex]-visited)

    return visited
