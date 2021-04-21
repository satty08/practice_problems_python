def beautifulArray(N):
    res = []
    if N%2 == 0:
        e, o = [], []
        for i in range(1, N+1):
            if i%2 == 0:
                e.append(i)
            else:
                o.append(i)
        i, j = 0, 0
        while i  < len(e) and j < len(o):
            if (i+j)%2 == 0:
                res.append(e[i])
                i += 1
            else:
                res.append(o[j])
                j += 1
        res.append(o[-1])
        return res
    
    else:
        e, o = [], []
        for i in range(1, N+1):
            if i%2 == 0:
                e.append(i)
            else:
                o.append(i)
        i, j = 0, 0
        mid = (N+1)//2
        res.append(mid)
        if mid in o:
            o.remove(mid)
        else:
            e.remove(mid)
        while i  < len(e) and j < len(o):
            if (i+j)%2 != 0:
                res.append(e[i])
                i += 1
            else:
                res.append(o[j])
                j += 1
        res.append(e[-1])
        return res

print(beautifulArray(7))

'''
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots 
i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing 
spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.
'''

def maxScoreSightseeingPair(values):
    ind, val = 0, values[0]
    res = 0
    for i in range(1,len(values)):
        res = max(res, values[i]+val-i+ind)
        if val - values[i] < i-ind:
            val = values[i]
            ind = i
    return res

from Day73 import totalMoney

print(totalMoney(9))