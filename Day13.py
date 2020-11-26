'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.
'''

def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i+1] <= nums[i]:
        i -= 1
    if i >= 0:
        j = len(nums) -1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        swap(nums, i ,j)
    reverse(nums, i+1)
    return nums
        
def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
        
def reverse(nums, start):
    i = start
    j = len(nums) - 1
    while i < j:
        swap(nums, i, j)
            
        i += 1
        j -= 1

nums = [1,2,3]
print(nextPermutation(nums))

'''
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already 
sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
'''

def inversion(arr, n):
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                res += 1
    return res
arr = [2, 4, 1, 3, 5]
print(inversion(arr, len(arr)))

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an 
algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''

def maxProfit(prices):
    minprice = 10**9
    maxprofit = 0
    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif prices[i] - minprice > maxprofit:
            maxprofit = prices[i] - minprice
    return maxprofit