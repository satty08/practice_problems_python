'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are 
drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis 
forms a container, such that the container contains the most water.
'''

def maxArea(self, height):
    res = []
    i = 0
    j = len(height) - 1
    while i < j:
        if height[i] < height[j]:
            res.append(height[i]*(j-i))
            i += 1
        else:
            res.append(height[j]*(j-i))
            j -= 1
                
    return max(res)

'''
Given two arrays: arr1[0..m-1] of size m and arr2[0..n-1] of size n. Task is to check whether arr2[] is a 
subset of arr1[] or not. Both the arrays can be both unsorted or sorted. It may be assumed that elements 
in both array are distinct.
'''

t = int(input())

while t:
    m,n = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    if n > m:
        print('No')
    else:
        flag = 0
        for i in range(n):
            if arr2[i] in arr1:
                continue
            else:
                flag = 1
                break
        if flag == 0:
            print('Yes')
        else:
            print('No')
    
    t -= 1