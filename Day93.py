'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
'''

def trap(height):
    n = len(height)
    if n == 0:
        return 0

    ans = 0
    leftMax = [0]*n
    rightMax = [0]*n

    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(height[i], leftMax[i-1])

    rightMax[n-1] = height[n-1]
    for j in range(n-2, -1, -1):
        rightMax[j] = max(height[j], rightMax[j+1])

    for i in range(1, n-1):
        ans += min(leftMax[i], rightMax[i]) - height[i]

    return ans

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''

def rotate(matrix):
    n = len(matrix[0])
    for i in range(n//2 + n%2):
        for j in range(n//2):
            temp = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[i][j]
            matrix[i][j] = temp