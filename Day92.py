'''
Count Primes
'''
def isPrime(a, arr):
    
    for i in arr:
        if a%i == 0:
            return False
    return True    

def countPrime(n):
    primes = [2,3,5,7,11,13,17,19]
    count = 0
    if n < primes[-1]:
        for i in primes:
            if n > i:
                count += 1
        return count

    count = len(primes)
    for i in range(20, n+1):
        if isPrime(i, primes):
            count += 1
            if i not in primes:
                primes.append(i)
    return count

# print(countPrime(1000000))
from collections import deque
def number(digits):
    if len(digits) == 0:
        return []

    d = {
        '1':'',
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
        '0':' '
    }

    res = deque()
    res.append('')

    for i in digits:
        for _ in range(len(res)):
            base = res.popleft()
            for c in d[i]:
                x = base+c
                res.append(x)


    return res

print(number('45837'))

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParenthesis(n):
    ans = []
    def backtrack(S=[],left=0, right=0):
        if len(S) == 2*n:
            ans.append(''.join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S,left+1, right)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S,left, right+1)
            S.pop()
        
    backtrack()
    return ans

#Brute Force Approach

        
#def generateParenthesis(n):      
#   def generate(A=[]):
#       if len(A) == 2*n:
#           if valid(A):
#               ans.append("".join(A))                
#       else:
#           A.append('(')
#           generate(A)
#           A.pop()
#           A.append(')')
#           generate(A)
#           A.pop()         
#   def valid(A):
#       bal = 0
#       for c in A:
#           if c == '(': bal+=1
#           else: bal -= 1         
#           if bal < 0: return False     
#       return bal == 0
#   ans = []
#   generate()
#   return ans


arr = [1,23,4,6,4,6,7,9]
n = len(arr)
k = 3
print(arr[n-1:n-1:-1])