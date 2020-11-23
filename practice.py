t = int(input())
for i in range(t):
    K, X = map(int, input().split())
    if X%K == 0:
        print(X-1)
    else:
        print(X+1)