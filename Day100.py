n = 15
for i in range(16):
    print(bin(i))

'''
Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest 
contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment 
of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies 
if there are no 1s.
'''

def checkZeroOnes(s):
    if '1' not in s:
        return False
    elif '0' not in s:
        return True
    
    else:
        ones, zero = 0, 0
        curr1, curr0 = 0, 0
        
        for i in s:
            if i == '1':
                curr1 += 1
                ones = max(ones, curr1)
                curr0 = 0
            else:
                curr0 += 1
                zero = max(zero, curr0)
                curr1 = 0
                
        return ones > zero         

arr = [-1,2,3]
n = list(set(arr))
n.sort()
print(n)

'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''

def validMountainArray(arr):
    n = len(arr)
    i = 0
    while i+1 < n and arr[i] < arr[i+1]:
        i += 1
        
    if i == 0 or i == n-1:
        return False
    
    while i+1 < n and arr[i] > arr[i+1]:
        i += 1
        
    return i == n-1