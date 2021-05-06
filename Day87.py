arr = [1,2,3,4,5,6]

for i, n in enumerate(arr):
    print(i, n)

'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
'''

def jump(nums):
    dp = [0 for i in range(len(nums))]
    for i,n in enumerate(nums):
        for j in range(1,n+1):
            if i+j < len(nums):
                if dp[i+j] == 0:
                    dp[i+j] = dp[i]+1

                else:
                    dp[i+j] = min(dp[i]+1, dp[i+j])

    return dp[-1]

#BFS Approach

def solve(nums):
    target, end, start, step = len(nums)-1,0,0,0
    while end < target:
        step += 1
        maxend = end + 1
        for i in range(start, end+1):
            if i+nums[i] >= target:
                return step
            maxend = max(maxend, i+nums[i])

        start, end = end+1, maxend

    return step