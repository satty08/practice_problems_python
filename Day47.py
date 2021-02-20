'''
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two 
consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7
'''

def numberOfArithmeticSlices(self, A):
    dp = 0
    res = 0
    for i in range(2, len(A)):
        if A[i] - A[i-1] == A[i-1] - A[i-2]:
            dp += 1
            res += dp
        else:
            dp = 0
                
    return res