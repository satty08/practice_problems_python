try:
    t = int(input())
    while t:
        n, e, h, a, b, c = map(int, input().split())
        mn = 10**9
        cnt, ck = 0, 0
        for k in range(min(e,h)):
            for i in range((e-k), 2):
                for j in range((h-k), 3):
                    cnt += k + i//2 + j//3
                    if cnt >= n:
                        mn = min(mn, k*c + a*(i//2) + b*(j//3))
                        ck = cnt
                    cnt = 0
        if ck < n:
            print(-1)
        else:
            print(mn)
        
        t -= 1
except:
    pass