'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
'''

def checkPossibility(nums):
    res,cnt = 0,0
    for i in range(1, len(nums)):
        if nums[i-1] <= nums[i]:
            res = nums[i-1]
        elif res <= nums[i]:
            cnt += 1
            
        else:
            nums[i]=nums[i-1]
            cnt += 1
            
        if cnt > 1:
            return False
        
    return True

#Brute Force Approach(WA)

# def checkPossibility(nums):
#     count = 0
#     if list(set(nums)) != nums:
#         return False
#     for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             count += 1
            
#         if count > 1:
#             return False
        
#     return True

'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):
    res = 0
    curr = 0
    start = 0
    ans = set()
    for i in s:
        curr += 1
        while i in ans:
            ans.remove(s[start])
            curr -= 1
            start += 1
        res = max(res, curr)
        ans.add(i)
        
    return res

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''

def findMedianSortedArrays(nums1, nums2):
    res = []
    for i in range(len(nums1)):
        res.append(nums1[i])
        
    for j in range(len(nums2)):
        res.append(nums2[j])
        
    res.sort()
    print(res)
    if len(res)%2 != 0:
        x = int((len(res))//2)
        return res[x]
    
    else:
        x, y = (len(res)//2 -1), len(res)//2
        return (res[x]+res[y])/2