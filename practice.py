n = int(input())
speed = list(map(int, input().split()))
res = 1
for i in range(1, n):
    if speed[i] < speed[i-1]:
        res += 1
print(res)