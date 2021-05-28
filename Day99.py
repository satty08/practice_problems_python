'''
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, 
if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of 
them. It is guaranteed that there will be at least one valid solution for the given input.
'''
def groupThePeople(groupSizes):
    res = []
    ans = {}
    
    for i in range(len(groupSizes)):
        if groupSizes[i] not in ans:
            ans[groupSizes[i]] = [i]
        else:
            ans[groupSizes[i]].append(i)
            
    for key, value in ans.items():
        if key != len(value):
            for i in range(0, len(value), key):
                res.append(value[i:i+key])
        else:
            res.append(value)
    return res
