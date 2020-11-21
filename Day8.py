'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by 
increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
'''
def minHeight(arr, n, k):
    if n == 1:
        return 0
    arr.sort()
    ans = arr[n-1] - arr[0]
    small = arr[0] + k
    big = arr[n-1] - k
    if small > big:
        small, big = big, small
    for i in range(1, n-1):
        sub = arr[i] - k
        add = arr[i] + k
        if (sub >= small) or (add <= big):
            continue
        if big-sub <= add-small:
            small = sub
        else:
            big = add
    return min(ans, big-small)
k = 2
n = 4
Arr= [1, 5, 8, 10]

x = minHeight(Arr, n, k)
print(x)

'''
Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then cannot move through that element.
'''

def minJumps(arr, n):
    count = 0
    i = 0
    while i < n:
        count += 1
        i += arr[i]
    return count 

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

print(minJumps(arr, len(arr)))

'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.
'''

def findDuplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            return nums[i]
    return False
nums = [1,3,4,2,2]
print(findDuplicate(nums))