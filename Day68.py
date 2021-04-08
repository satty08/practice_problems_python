'''
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] 
(i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that 
all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.
'''

def minOperations(n):
    res = []
    for i in range(n):
        res.append(2*i + 1)
    lo, hi = 0, n-1
    ans = 0
    while lo <= hi:
        ans += (res[hi] - res[lo])//2
        lo += 1
        hi -= 1
    return ans


try:
    t = int(input())
    while t:
        n, m, k = map(int, input().split())
        arr = []
        for i in range(n):
            x = list(map(int, input().split()))
            arr.append(x)
        print(arr)
        v, l = 0, 0
        minNM = min(n, m)
        while l < minNM:
            l += 1
            if l == 1:
                for i in range(n):
                    for j in range(m):
                        if arr[i][j] >= k:
                            v += 1
            else:
                for i in range(n-l):
                    for j in range(m-l):
                        Sum = 0
                        for x in range(j, j+l):
                            for p in range(i, i+l):
                                Sum += arr[p][x]
                                
                        avg = Sum//(l*l)
                        if avg >= k:
                            v += m-l+1-j
                            break
                        
        print(v)
        t -= 1
except:
    pass