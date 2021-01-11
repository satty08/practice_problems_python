# a = int(input())
# n = int(input())
# x = list(map(int, input().split()))
# b = 0
# i = 0
# res = 1
# while n > 0:
#     power = 10**(n-1)
#     b = res*(a**(x[i]*power))
#     res = b%1337
#     n -= 1
#     i += 1
# print(res)

# t = int(input())
# while t:

#     n = int(input())
#     strength = list(map(int, input().split()))
#     count = 0
#     for i in range(n):
#         for j in range(i, n):
#             if strength[i] > 2*strength[j]:
#                 count += 1
#     print(count)
#     t -= 1
# 1 3 2 6 2 7 4 2 3 1

# t = int(input())
# while t:
#     x, y = map(int, input().split())
#     if x == 1 or y == 1:
#         res = (x+y)//2
#         print(res)
#     else:
#         res = (x*y)//2
#         print(res)
#     t-=1

# import math
# n, d = map(int, input().split())
# ages = list(map(int, input().split()))
# risk, noRisk = 0, 0
# for i in range(n):
#     if ages[i] >= 80 or ages[i] <= 9:
#         risk += 1
#     else:
#         noRisk += 1
# days = math.ceil(risk/d) + math.ceil(noRisk/d)
# print(days)

# def firstNotRepeatingCharacter(s):
#     res = {}
#     for i in range(len(s)):
#         if s[i] not in res:
#             res[s[i]] = 1
#         else:
#             res[s[i]] += 1
#     ans=""
#     for key in res:
#         if res[key] == 1:
#             ans = key
#             break
#     return ans

# s = "absbabsnsaks"

# print(firstNotRepeatingCharacter(s))

res = []
n, k = map(int, input().split())
for i in range(1,n+1):
    res.append(str(i))
x = " ".join(res)
print(x)

def isCryptSolution(crypt, solution):
    res = {}
    for i in range(len(solution)):
        res[solution[i][0]] = solution[i][1]
    x = 0
    for i in range(len(crypt)-1):
        a = ''
        for j in crypt[i]:
            if j in res:
                a += res[j]
        if len(crypt[i]) != len(str(int(a))):
            return False
        print(a)
        x += int(a)
    a=''
    for j in crypt[2]:
        if j in res:
            a += res[j]
    if len(crypt[2]) != len(str(int(a))):
        return False
    if x == int(a):
        return True
    else:
        return False

crypt = ["WASD", 
 "IJKL", 
 "AOPAS"]
solution = [["W","2"], 
 ["A","0"], 
 ["S","4"], 
 ["D","1"], 
 ["I","5"], 
 ["J","8"], 
 ["K","6"], 
 ["L","3"], 
 ["O","7"], 
 ["P","9"]]
# print(isCryptSolution(crypt, solution))

def processQueries(queries, m):
    P = [i+1 for i in range(m)]
    res = []
    for i in range(len(queries)):
        n = P.index(queries[i])
        res.append(n)
        P.insert(0,P.pop(n))
    return res

queries=[3, 1, 2, 1]
m = 5
print(processQueries(queries, m))