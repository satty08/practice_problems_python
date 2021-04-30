'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
'''

def searchRange(nums, target):
    if nums == []:
        return [-1, -1]
    
    if target not in nums:
        return [-1, -1]
    
    x = nums.count(target)
    
    if x == 1:
        y = nums.index(target)
        return [y, y]
    else:
        for i in range(len(nums)):
            if nums[i] == target:
                a = i
                break
                
        return [a, a+x-1]