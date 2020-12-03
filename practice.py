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

from itertools import permutations as p

string = 'abcde'
perm = p(string)
x = list(perm)
print(x)