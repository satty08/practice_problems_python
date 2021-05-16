'''
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. 
Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle 
are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
'''
import math
def countPoints(points, queries):
    res = []
    
    for i in queries:
        count = 0
        for j in points:
            x = abs(i[0]-j[0])
            y = abs(i[1]-j[1])
            dist = math.sqrt(pow(x,2)+pow(y,2))
            if dist <= i[2]:
                count += 1
                
        res.append(count)
        
    return res

