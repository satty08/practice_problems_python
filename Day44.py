'''
Given an array of size N. The task is to sort the array elements by completing functions heapify() and 
buildHeap() which are used to implement Heap Sort.
'''

def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''
    # code here
    large = i
    l = 2*i + 1
    r = 2*i + 2
    
    if l < n and arr[large] <= arr[l]:
        large = l
        
    if r < n and arr[large] <= arr[r]:
        large = r
        
    if large != i:
        temp = arr[i]
        arr[i] = arr[large]
        arr[large] = temp
        heapify(arr, n, large)

def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''
    # code here
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range((n-1), 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
