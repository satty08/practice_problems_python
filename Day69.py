'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the 
first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
'''

def halvesAreAlike(self, s: str) -> bool:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    mid = (0+len(s))//2
        
    a = s[:mid]
    b = s[mid:]
    aCount, bCount = 0, 0
    for i in a:
        if i in vowels:
            aCount += 1
    for i in b:
        if i in vowels:
            bCount += 1
                
    return aCount == bCount

num = -7
num = int(str(num)[1:])
print(num)