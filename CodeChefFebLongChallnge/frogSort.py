t = int(input())
while t > 0:
    n = int(input())
    W = list(map(int, input().split()))
    L = list(map(int, input().split()))
    x = sorted(W)
    pos = []
    for i in range(n):
        pos.append(i)
    count = 0
    for i in range(1, n):
        index = W.index(x[i])
        p = pos[W.index(x[i])]
        c = index

        while c <= p:
            c += L[index]
            pos[index] = x
            count += 1

    print(count+1)

    t -= 1