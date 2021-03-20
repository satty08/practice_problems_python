'''
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
'''

def addToArrayForm(A, K):
    x = 0
    a = len(A)-1
    for i in range(len(A)):
        x += A[i]*(10**a)
        a -= 1
            
    x += K
    res = []
    while x > 0:
        res.append(x%10)
        x = x//10
            
    return res[::-1]

print(addToArrayForm([0], 0))

'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''
def addDigits(num):
    while num > 9:
        res = []
        while num > 0:
            res.append(num%10)
            num = num//10
                
        num = sum(res)
            
    return num
