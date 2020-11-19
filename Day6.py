'''
Write a Python function to return minimum and maximum in an array. You program should make minimum number of comparisons. 
'''

def compare(arr):
    maxno = -10**9
    minno = 10**9
    for i in range(len(arr)):
        if arr[i] > maxno:
            maxno = arr[i]
        if arr[i]  < minno:
            minno = arr[i]
    return maxno, minno

arr = [12, 3, 6, 13, 123, 68, 124, 12345]

print(compare(arr))

'''
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest 
element in the given array. It is given that all array elements are distinct.
'''

def findElement(arr, k):
    arr.sort()
    return arr[k-1]
arr = [12, 4, 32, 45, 11, 78, 23, 56]
print(findElement(arr, 4))

'''
Given an array of size N containing 0s, 1s, and 2s; sort the array in ascending order.
'''

def sort012(arr,n):
    lo = 0
    hi = n-1
    mid = 0
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr

arr = [0,1,1,0,2,2,2,2,1,1,0,1,2,1,0]
print(sort012(arr, len(arr)))

'''
Move all negative numbers to beginning and positive to end with constant extra space.
'''

def oneSide(arr, n):
    side = 0
    i = 0
    while i < n:
        if arr[i] < 0:
            arr[i], arr[side] = arr[side], arr[i]
            side += 1
        i += 1
        
    return arr
    
arr = [12, 3, -4, 0, -6, 23, 45, -1]

print(oneSide(arr, len(arr)))