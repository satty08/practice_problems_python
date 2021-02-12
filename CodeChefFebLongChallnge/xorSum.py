from itertools import permutations

def xorSum(arr, n):
    perm = permutations(arr, n)
    for i in list(perm):
        res = 0
        for j in range(len(i)):
            res += res | i[j]
    return res

n = int(input())
nval = list(map(int, input().split()))
q = int(input())
qval = []
for i in range(q):
    qval.append(int(input()))
res = {}
for i in qval:
    if i == 1:
        print(sum(nval))

        continue

    for j in range(1, i+1):
        res[j] = xorSum(nval, i)
    print(sum(res.values()))