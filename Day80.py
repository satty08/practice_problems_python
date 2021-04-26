'''
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied 
by its satisfaction level  i.e.  time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
'''

def maxSatisfaction(satisfaction):
    def dp(arr):
        y = 0
        for i in range(len(arr)):
            y += arr[i]*(i+1)
            
        return y
    satisfaction.sort()
    res = 0
    for i in range(len(satisfaction)):
        x = dp(satisfaction[i:len(satisfaction)])
        res = max(res, x)
        
    return res