def minCntFount(a, N):
    dp = [0]*N
    for i in range(N):
        idxLeft = max(i-a[i], 0)
        idxRight = min(i+(a[i]+1), N)
        dp[idxLeft] = max(dp[idxLeft], idxRight)

    cntFount = 1

    idxRight = dp[0]
    
    idxNext = 0

    for i in range(N):
        idxNext = max(idxNext, dp[i])

        if i == idxRight:
            cntFount += 1
            idxRight = idxNext

    return cntFount

a = [2,1,1,2,1, 2,3,2,4]
print(minCntFount(a, len(a)))

'''
Given an array arr[] of size N and two integers M and K, the task is to find the array element at the Kth index after 
performing following M operations on the given array.

In a single operation, a new array is formed whose elements have the Bitwise XOR values of the adjacent elements of the 
current array.

If the number of operations M or the value of K after M operations is invalid then print -1.
'''

def xor(a, m, k):
    n = len(a)
    if m < 0 or m > n:
        return -1

    if k < 0 or k >n-m:
        return -1

    while m:
        res = []
        for i in range(len(a) - 1):
            res.append(a[i]^a[i+1])

        a = res[:]

        m -= 1 

    return a[k]

a = [1,4,5,6,7]
print(xor(a, 1, 2))

'''
Given an integer N, the task is to check if N can be expressed as a sum of integers having 9 as the last digit 
(9, 19, 29, 39…), or not. If found to be true, then find the minimum count of such integers required to obtain N. 
Otherwise print -1.
'''

def sum0fnine(n):
    k = n%10

    a = 9*(9-k)

    z = n - a

    if z >= 9 and z%10 == 9:
        return 10 - k
    else:
        return -1

print(sum0fnine(60))