'''
Find the Union and Intersection of the two sorted arrays.
'''

def union(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    count = 0
    if n < m:
        for i in range(n):
            if arr1[i] in arr2:
                count += 1
    else:
        for i in range(m):
            if arr2[i] in arr1:
                count += 1
                    
    n = n-count
    m = m-count
    return n+m+count
def intersection(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    count = 0
    if n < m:
        for i in range(n):
            if arr1[i] in arr2:
                count += 1
    else:
        for i in range(m):
            if arr2[i] in arr1:
                count += 1
    return count

arr1 = [1,2,3,4,5,6]
arr2 = [5,6,7,8,9]
print(union(arr1, arr2))
print(intersection(arr1, arr2))

'''
Given an array, cyclically rotate an array by one.
'''

def rotate(arr):
    n = len(arr)
    res = []
    res.append(arr[n-1])
    for i in range(n-1):
        res.append(arr[i])
    return res

arr = [1,2,3,4,5]
print(rotate(arr))

'''
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
'''

def maxSubArraySum(a,size):
    ##Your code here
    currsum = a[0]
    ans = a[0]
    for i in range(1, size):
        currsum = max(currsum+a[i], a[i])
        ans = max(ans, currsum)
    return ans

arr = [1, -4, 5, 3, -2, 8]
print(maxSubArraySum(arr, len(arr)))