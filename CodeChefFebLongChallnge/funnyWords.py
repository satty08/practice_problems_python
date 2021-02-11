n = int(input())
name = list(map(str, input().split()))
res = 0
for i in range(n):
    for j in range(i+1, n):
        temp1 = name[i][0] + name[j][1:]
        temp2 = name[j][0] + name[i][1:]

        if temp1 not in name and temp2 not in name:
            res += 2

print(res)