'''
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.
'''


# Naive Approach
# def maxEnvelopes(envelopes):
#     envelopes.sort()
#     print(envelopes)
#     res = [envelopes[0]]
#     for i in range(1, len(envelopes)):
#         if (res[-1][0] < envelopes[i][0]) and (res[-1][1] < envelopes[i][1]):
#             res.append(envelopes[i])

#     print(res)
#     return len(res)

# DP Solution
import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key= lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            left = bisect.bisect_left(dp, h)
            if left == len(dp): dp.append(h)
            else: dp[left] = h
                
        return len(dp)

'''
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between 
every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only 
if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range 
queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can 
be rearranged to form an arithmetic sequence, and false otherwise. 
'''

class Solution1:
    def isArithmatic(self, arr):
        arr.sort()
        diff = abs(arr[0] - arr[1])
        for i in range(1, len(arr)-1):
            if abs(arr[i] - arr[i+1]) != diff:
                return False
        return True
    
    def checkArithmeticSubarrays(self, nums, l, r):
        res = []
        
        n = len(l)
        for i in range(n):
            x = nums[l[i]:r[i]+1]
            if self.isArithmatic(x):
                res.append(True)
            else:
                res.append(False)
                
        return res