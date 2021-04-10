try:
    t = int(input())
    while t:
        n, m, k = map(int, input().split())
        arr = list(map(int, input().split()))
        arrM = []
        for i in range(m):
            x = list(map(int, input().split()))
            arrM.append(x)

        
        t -= 1
except:
    pass