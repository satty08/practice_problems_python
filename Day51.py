'''
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, 
so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, 
and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if 
she only eats n / 2 of them.
'''

def distributeCandies(self, candyType):
    i = len(candyType)//2
    x = set(candyType)
    if i > len(x):
        return len(x)
    else:
        return i

'''
Quick Sort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position low and its ending position high.

Implement the partition() and quickSort() functions to sort the array.
'''

def quickSort(self,arr,low,high):
    # code here
    if low < high:
        pi = self.partition(arr, low, high)
        
        self.quickSort(arr, low, pi-1)
        self.quickSort(arr, pi+1, high)
    
def partition(self,arr,low,high):
    # code here
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1