'''
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.
'''

def powerfulIntegers(x, y, bound):
    res = []
    for i in range(50):
        for j in range(50):
            if (x**i + y**j) <= bound:
                res.append(x**i + y**j)
                
    res = set(res)
    
    return res