'''
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
'''

def solution(nums):
    nums.sort()
    res = 0
    for i in range(0, len(nums), 2):
        res += nums[i]
            
    return res

nums = [6,2,6,5,1,2]

print(solution(nums))

'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each 
cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.
'''

def findContentChildren(g, s):
    i, j, a = 0, 0, 0
    g.sort()
    s.sort()
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
            j += 1
            a += 1
        else:
            j += 1
    return a