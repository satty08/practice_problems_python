'''
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.
'''

class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zero = s.count('0')
            one = len(s) - zero
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero][j-one]+1)
        return dp[m][n]