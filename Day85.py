'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

def runningSum(nums):
    for i in range(1,len(nums)):
        nums[i] = nums[i-1] + nums[i]
        
    return nums


cup = [1,0,0]
n = int(input('How many times the cups are to be swapped? '))
for i in range(n):
    print('What cups do you want to swap between them? ')
    x = int(input())
    y = int(input())
    cup[x-1], cup[y-1] = cup[y-1], cup[x-1]

x = cup.index(1)+1
print('The cup that has the ball is: ', x)