'''
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
'''

def furthestBuilding(heights, bricks, ladders):

    # Min heap Approach
    gap = []
    length = len(heights)
    for i in range(length-1):
        curr = heights[i+1] - heights[i]
        if curr > 0:
            heappush(gap, curr)
        if len(gap) > ladders:
            climbHeight = heappop(gap)
            bricks -= climbHeight
            
        if bricks < 0:
            return i
    return length - 1

    #Brute Force Approach
    # res = 0
    # for i in range(len(heights)-1):
    #     if heights[i] >= heights[i+1]:
    #         res += 1
    #     elif heights[i] < heights[i+1]:
    #         if ladders > 0:
    #             ladders -= 1
    #             res += 1
    #         elif (heights[i+1]-heights[i]) <= bricks:
    #             bricks -= (heights[i+1]-heights[i])
    #             res += 1
    #         else:
    #             break
    # return res

import math
x = str(math.log(59049, 3))
print(x)
y = x.split('.')
if int(y[1]) != 0:
    print(False)
else: print(True)
print(243%3)

def solve(l, r):
    if l==r:
        return 1
    else:
        return solve(l+1, r) + solve(l, r-1)

v = solve(2, 5)
print(v)

def s(x):
    if x > 0:
        x -= 1
        s(x)
        print(x)

s(4)