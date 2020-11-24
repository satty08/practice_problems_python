g = int(input())
for i in range(g):
    res = 0
    i, n, q = map(int, input().split())
    if n%2 != 0:
        if i == 1 and q == 1:
            res = n//2
        elif i==1 and q == 2:
            res = n//2 + 1
        elif i == 2 and q == 1:
            res = n//2 + 1
        elif i == 2 and q == 2:
            res = n//2
    else:
        res = n//2
    print(res)