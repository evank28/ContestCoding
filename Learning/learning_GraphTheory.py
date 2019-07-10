#breadth first search
#from https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
from collections import deque

graph = {'A': set(['B', 'C']),          #adjacency list format  
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])} 

def iDFSl (graph, start):
    """
    Iterative Depth-First Search algorithmic method for a graph that is an adjacency list
    """
    visited = set()
    stack = [start]

    while stack:                                    #loops until stack is empty
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)                     #adds the vertext to the visited list
            stack.extend(graph[vertex]-visited)     #adds ONLY unvisited adjacencies to the stack

    return visited                                  #returns the set of all visited nodes

def iDFSl_path (graph, start, goal):
    """
    Iterative Depth-First Search algorithmic method for a graph that is an adjacency list. Returns the path to the goal.
    """
    visited = set()
    stack = [start]

    while stack:                                    #loops until stack is empty
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)                     #adds the vertext to the visited list
            stack.extend(graph[vertex]-visited)     #adds ONLY unvisited adjacencies to the stack

    return visited     


def rDFSl (graph, start, visited=None):
    """
    Recursive Depth-First Search algorithmic method for a graph that is an adjacency list
    """
    if visited is None:                              #rests visited on each call
        visited = set()

    visited.add(start)                              #adds the vertex to the visited list

    for next in graph[start]-visited:               #continues down ONLY unvisited adjacencies, before returning
        rDFSl(graph, next, visited)

    return visited


def iBFSl (graph, start):
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

"""
def aStar ()
"""    


def rBFSl (graph, start):
    if visited is None:                              #rests visited on each call
        visited = set()

    visited.add(start)

    for adj in graph[start]-visited:
        





