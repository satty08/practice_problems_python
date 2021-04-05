'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''

class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for i in asteroids:
            while res and i < 0 < res[-1]:
                if res[-1] < -i:
                    res.pop()
                    continue
                elif res[-1] == -i:
                    res.pop()
                break
            else:
                res.append(i)
        return res

def backspaceCompare(S, T):
    res = []
    for i in S:
        if i == '#' and len(res) > 0:
            res.pop()
        elif i == '#' and len(res) == 0:
            continue
        else:
            res.append(i)
        print(res)
    ans = []
    for i in T:
        if i == '#' and len(ans) > 0:
            ans.pop()
        elif i == '#' and len(ans) == 0:
            continue
        else:
            ans.append(i)
        print(ans)
                
    return res == ans

s = 'f#fo##f'
t = 'f#f#o##f'
print(backspaceCompare(s, t))

mat = [[1, 2], [3, 4]]
mat.append([0]*len(mat[0]))
for i in range(len(mat)):
    mat[i].append(0)

for i in range(len(mat)-1, -1, -1):
    for j in range(len(mat[i])-1, -1, -1):
        mat[i][j] = mat[i][j-1]
    mat[i][0] = 0
    mat[i] = mat[i-1]

mat[0] = [0]*(len(mat[0]))
print(mat)


def Solve(mat, n, m, k, order):
    cnt = 0
    minNM = min(n, m)
    while order <= minNM:
        i, j = order, m
        while i <= n:
            a, b = i-order+1, j-order+1
            c = mat[i][j] - mat[a-1][j] - mat[i][b-1] + mat[a-1][b-1]
            
            if (c//(order*order)) < k:
                i += 1
            else:
                lo, hi = order, m
                while lo <= hi:
                    mid = (lo+hi)//2
                    a = i-order+1
                    b = mid-order+1
                    c = mat[i][mid] - mat[a-1][mid] - mat[i][b-1] + mat[a-1][b-1]
                    if (c//(order*order)) < k:
                        lo = mid+1
                    else:
                        ans = mid
                        hi = mid-1
            cnt += m - ans + 1
            i += 1
        order += 1
        
    return cnt
    
try:
    t = int(input())
    while t:
        n, m, k = map(int, input().split())
        res = []
        for i in range(n):
            x = list(map(int, input().split()))
            res.append(x)
        for i in range(n):
            Sum = 0
            for j in range(m):
                Sum += res[i][j]
                res[i][j] = Sum
                
        for i in range(m):
            Sum = 0
            for j in range(n):
                Sum += res[i][j]
                res[i][j] = Sum
                
        res.append([0]*len(res[0]))
        for i in range(len(res)):
            res[i].append(0)
        
        for i in range(len(res)-1, -1, -1):
            for j in range(len(res[i])-1, -1, -1):
                res[i][j] = res[i][j-1]
            res[i][0] = 0
            res[i] = res[i-1]
        
        res[0] = [0]*(len(res[0]))
        print(Solve(res, n,m,k,1))
        t -= 1
except:
    pass
