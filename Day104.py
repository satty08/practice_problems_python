'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

def longestConsecutive(nums):
    if nums == []:
        return 0
    res, count = 0, 0
    num = list(set(nums))
    num.sort()
    i = 0
    while i < len(num)-1:
        if num[i+1] == num[i]+1:
            count += 1
            
        else:
            res = max(res, count)
            count = 0
        i += 1
        
    res = max(res,count)
    return res+1

