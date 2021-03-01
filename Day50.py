'''
Given a sorted array of size N and an integer K. Check if K is present in the array or not.
'''
# Binary Search
def searchInSorted(self,arr, N, K):
    #Your code here
    lo = 0
    hi = N-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == K:
            return 1
        elif arr[mid] < K:
            lo = mid + 1
        elif arr[mid] > K:
            hi = mid - 1
    return -1

'''
Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.
'''

# Selection Sort
def selectionSort(self, arr,n):
    #code here
    for i in range(n):
        idx = i
        for j in range(i+1, n):
            if arr[idx] > arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

'''
Given an Integer N and a list arr. Sort the array using bubble sort algorithm.
'''

def bubbleSort(self,arr, n):
    # code here
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

'''
Given an Integer N and a list arr. Sort the array using insertion sort algorithm.
'''

def insertionSort(self, arr, n):
    #code here
    for i in range(n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr