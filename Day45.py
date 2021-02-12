'''
Given an array A of size N, the task is to check if the given array represents a Binary Max Heap.
'''

def arrayRepresentHeap(arr,n):
    # Your code goes here            
    for i in range((n-2)//2 + 1):
        if arr[2*i+1] > arr[i]:
            return 0
            
        if (2*i+2 < n) and arr[2*i+2] > arr[i]:
            return 0
            
    return 1

