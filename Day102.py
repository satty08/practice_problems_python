'''
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts 
where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, 
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the 
arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.
'''

def maxArea(h, w, horizontalCuts, verticalCuts):
    horizontalCuts.sort()
    verticalCuts.sort()
    n, m = len(horizontalCuts), len(verticalCuts)
    
    maxH = [horizontalCuts[0]]
    maxW = [verticalCuts[0]]
    
    for i in range(1, n):
        maxH.append(horizontalCuts[i] - horizontalCuts[i-1])
        
    maxH.append(h - horizontalCuts[n-1])
    
    for j in range(1, m):
        maxW.append(verticalCuts[j] - verticalCuts[j-1])
        
    maxW.append(w - verticalCuts[m-1])
    
    ans = max(maxH)*max(maxW)
    
    return ans%(10**9+7)

'''
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such 
that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest 
vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
'''

def maxWidthOfVerticalArea(points):
    arr = [0]*len(points)
    
    for i in range(len(points)):
        arr[i] = points[i][0]
        
    arr.sort()
    ans = 0
    
    for i in range(0, len(points)-1):
        ans = max(ans, arr[i+1] - arr[i])
        
    return ans

'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths 
from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
(i.e., there is a directed edge from node i to node graph[i][j]).
'''

def allPathsSourceTarget(graph):
    res = []
    n = len(graph)
    
    def dfs(path, idx, n):
        if idx == n-1:
            res.append(path.copy())
        else:
            for i in graph[idx]:
                path.append(i)
                dfs(path, i, n)
                path.pop()
    
    
    dfs([0], 0, n)
    return res