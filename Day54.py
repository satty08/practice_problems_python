'''
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. 
Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
'''

def numFactoredBinaryTrees(arr):
    mod = 10**9 + 7
    n = len(arr)
    arr.sort()
    dp = [1]*n
    idx = {x: i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        for j in range(i):
            if x%arr[j] == 0:
                right = x//arr[j]
                if right in idx:
                    dp[i] += dp[j]*dp[idx[right]]
                    dp[i] %= mod
                        
    return sum(dp)%mod