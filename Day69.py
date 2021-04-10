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


p = 0
for i in range(6):
    for j in range(2, 6):
        for k in range(1, 6):
            p += 1

print(p)
k = ord('a')
print(k)


def solve(n, m, k):
    for i in range(n+1):
        prev = 0
        for j in range(m+1):
            arr[i][j] += prev
            prev = arr[i][j]
    print(arr)
    for i in range(m+1):
        prev = 0
        for j in range(n+1):
            arr[j][i] += prev
            prev = arr[j][i]
    print(arr)
    m_min = min(m, n)
    res = 0
    for x in range(1, m_min+1):
        for i in range(x, n+1):
            for j in range(x, m+1):
                if ((arr[i][j]+arr[i-x][j-x]-arr[i][j-x] - arr[i-x][j])//(x*x) >= k):
                    res += 1
    return res

try:
    t = int(input())
    while t:
        n, m, k = map(int, input().split())
        arr = []
        for i in range(n):
            x = list(map(int, input().split()))
            x.insert(0, 0)
            arr.append(x)
        arr.insert(0, [0]*(len(arr[0])))
                        
        print(solve(n, m, k))
        t -= 1
except:
    pass
