'''
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and 
arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.
'''

def threeSumMulti(arr, target):
    d = [0]*300
    res = 0
    for i in range(len(arr)):
        res += d[target-arr[i]] if target-arr[i] >= 0 else 0
        res%=(10**9+7)
        for j in range(i):
            d[arr[i]+arr[j]] += 1
                
    return res%(10**9+7)

