'''
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

def uniqueString(s):
    x = len(s)
    for i in range(x):
        if s[i] in s[i+1:]:
            return False
    return True

s = 'arora'
print(uniqueString(s))

'''
Given two strings, write a method to decide if one is a permutation of the other.
'''
from itertools import permutations as p

def isPermutation(x, y):
    permX = p(x)
    for i in list(permX):
        ans = ''
        for j in range(len(i)):
            ans += i[j]
        if ans == y:
            return True
    return False
x = 'arora'
y = 'roara'
print(isPermutation(x, y))