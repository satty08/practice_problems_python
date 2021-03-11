import bisect

try:
    t = int(input())
    while t:
        n, e, h, a, b, c = map(int, input().split())
        vec = []
        kvec = []
        for i in range(n+2):
            kvec.append(i)

        for m in range(n+1):
            index1 = bisect.bisect_left(kvec, 2*n-e-2*m, 0, len(kvec))
            index2 = bisect.bisect_right(kvec, h-3*m-1, 0, len(kvec))

            if index2 < index1 or index1 == n+1:
                continue
            if index2 == n+1 and index2+3*m > h:
                continue

            if c > a:
                k = index1 if index1 < (n-m) else n-m
            else:
                k = index2 if index2 < (n-m) else n-m

            o = n-k-m

            if k+2*m >= 2*n-e and k+3*m <= h:
                vec.append(a*o+b*m+c*k)

        if len(vec) == 0:
            print(-1)
        else:
            print(min(vec))

        t -= 1
except:
    pass