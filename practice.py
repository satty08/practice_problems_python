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

# res = []
# n, k = map(int, input().split())
# for i in range(1,n+1):
#     res.append(str(i))
# x = " ".join(res)
# print(x)

# def isCryptSolution(crypt, solution):
#     res = {}
#     for i in range(len(solution)):
#         res[solution[i][0]] = solution[i][1]
#     x = 0
#     for i in range(len(crypt)-1):
#         a = ''
#         for j in crypt[i]:
#             if j in res:
#                 a += res[j]
#         if len(crypt[i]) != len(str(int(a))):
#             return False
#         print(a)
#         x += int(a)
#     a=''
#     for j in crypt[2]:
#         if j in res:
#             a += res[j]
#     if len(crypt[2]) != len(str(int(a))):
#         return False
#     if x == int(a):
#         return True
#     else:
#         return False

# crypt = ["WASD", 
#  "IJKL", 
#  "AOPAS"]
# solution = [["W","2"], 
#  ["A","0"], 
#  ["S","4"], 
#  ["D","1"], 
#  ["I","5"], 
#  ["J","8"], 
#  ["K","6"], 
#  ["L","3"], 
#  ["O","7"], 
#  ["P","9"]]
# # print(isCryptSolution(crypt, solution))

# def processQueries(queries, m):
#     P = [i+1 for i in range(m)]
#     res = []
#     for i in range(len(queries)):
#         n = P.index(queries[i])
#         res.append(n)
#         P.insert(0,P.pop(n))
#     return res

# queries=[3, 1, 2, 1]
# m = 5
# print(processQueries(queries, m))

# import timeit
# negSum = 0

# for i in range(10000000):
#     start = timeit.default_timer()
#     negSum -= 1
# stop = timeit.default_timer()

# print(negSum)
# print(stop-start)
# def lcs(X, Y, m, n):
#     if m == 0 or n == 0:
#         return 0
#     elif X[m-1] == Y[n-1]:
#         return 1 + lcs(X, Y, m-1, n-1)
#     else:
#         return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

# X = 'abcda'
# Y = 'cbadca'
# m = 5
# n = 6
# print(lcs(X, Y, m, n))

# import math

# print(math.sqrt(25))
# print(math.pi*5*5)
# sinefunction = math.sin(180)
# cosinefunc = math.cos(180)
# print(sinefunction, cosinefunc)

# import random

# print(random.randrange(0,5))
# print(random.uniform(0, 1))
# print(random.randint(0, 100))
# List = [1, 4, True, 800, "python", 27, "hello"]
# item = int(random.uniform(0,1)*6)
# print(List[item])

# import time

# seconds = time.time()
# print(seconds)

# local_time = time.ctime(1612100010.7453306)
# print(local_time)

# print("This is printed immediately.")
# time.sleep(2.4)
# print("This is printed after 2.4 seconds.")

# t = input()
# res = list(t.split(' '))
# for i in range(len(res)):
#     print(res[i][::-1])
    
# def stepIncreaseList(arr, n):
#     if n == 0:
#         return True
    
#     if arr[n-1] > arr[n-2]:
#         return stepIncreaseList(arr, n-2)
#     else:
#         return False

# L1 = [1, 21, 8, 1, 4, 10, 8, 12]
# print(stepIncreaseList(L1, 8))

# n = 11
# x = bin(n).replace('0b', '')
# print(type(x))


# t = int(input())
# while t:
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     sum_t = abs(arr[0]-arr[1])+ abs(arr[0]-arr[n-1])+ abs(arr[n-1]-arr[1])
#     print(sum_t)
#     t -= 1

# s = 'aaab'
# res = []
# count = 0
# for i in s:
#     if i == 'b':
#         res.append(count)
#     count += 1
# ans = []
# for i in range(len(s)):
#     diff = 10**9
#     for j in res:
#         diff = min(diff, abs(i-j))
#     ans.append(diff)

# print(ans)







# time = list(map(str, input().split()))
# print(time)
# if time[1] == 'AM':
#     res = list(map(int, time[0].split(':')))
#     if res[0] == 12:
#         t = res[1]
#     else:
#         t = res[0]*100 + res[1]

# elif time[1] == 'PM':
#     res = list(map(int, time[0].split(':')))
#     if res[0] == 12:
#         t = res[0]*100 + res[1]
#     else:
#         t = 1200 + res[0]*100 + res[1]

# print(t)

# from itertools import permutations

# arr = [1,3,5,2]
# perm = permutations(arr, 1)
# for i in list(set(perm)):
#     print(i)

# mat = [
#     [1,1,1,0,0],
#     [1,1,0,0,0],
#     [0,0,0,0,0]
# ]
# k = 2
# ans = {}
# for i in range(len(mat)):
#     ans[i] = mat[i].count(1)
# res = []
# while k > 0:
#     res.append(min(ans, key=ans.get))
#     ans.pop(min(ans, key=ans.get))
#     k -= 1

# print(res)

# res = []
# n = int(input())
# while n>0:
#     curr1, curr2 = list(map(str, input().split()))
#     if curr1 == 'MainQueue':
#         res.append(curr2)
#     elif curr1 not in res:
#         print('Invalid Input')
#         continue
#     elif curr1 in res:
#         temp = res.index(curr1)
#         res.insert(temp+1, curr2)

#     n -= 1
# print(res)

# s = "a1b2"
# def letterCase(s):
#     res = set()
#     tmp = 0
#     curr = list(s)
#     for i in s:
#         if i.isalpha():
#             tmp += 1
#     tmp = 2**tmp
    
# print(letterCase(s))

# def romanToInt(s):
#     d = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     out = 0
#     for i in range(len(s)-1):
#         print(d[s[i]])
#         if d[s[i]]<d[s[i+1]]:
#             out -= d[s[i]]
#         else:
#             out += d[s[i]]
#     out+= d[s[-1]]
#     return out

# import math

# res = math.sin(math.pi/2)
# print(res)

# s = 'abpcplea'
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# t = 'apple'
# flag = 0
# for i in t:
#     s = t.count(i)
#     if d[i] < s:
#         flag = 1
#         break

# if flag == 1:
#     print('False')
# else:
#     print(True)

def findUnsortedSubarray(nums):
    x = sorted(nums)
    start, end = len(nums), 0
    for i in range(len(x)):
        if x[i] != nums[i]:
            start = min(start, i)
            end = max(end, i)
            print(start, end)
                
    if end - start > 0:
        return end - start + 1
    else:
        return 0

# nums = [2,6,4,8,10,9,15]
# print(findUnsortedSubarray(nums))

# temp = [12,45,24,12,67,34,23,89,34,89,23,89,12,78,90,67]
# k = int(input())
# index = int(input())
# avg = (sum(temp[index-k:index]) + temp[index] + sum(temp[index+1:index+k+1]))/(2*k+1)
# print(avg)

# n = int(input())
# while n:
#     x = int(input())
#     flag = False
#     while x > 0:
#         for i in range(1, x+1):
#             if (i & x) == 0:
#                 flag = not flag
#                 break
#         x -= i
#     if flag == False:
#         print('Vaibhavi')
#     else:
#         print('Anjali')

#     n -= 1

class X:
    def __init__(self, arr):
        self.arr = arr

    def insert(self,x):
        if x not in self.arr:
            self.arr.append(x)

        return self.arr
    
    def delete(self,x):
        if x in self.arr:
            self.arr.remove(x)
        
        return self.arr

    def find__smallest(self,k):
        arr1 = self.arr
        while k > 1:
            x = min(arr1)
            arr1.remove(x)
            k -= 1

        return min(arr1)

arr = [4,5,1,7,2,9,6]

x = X(arr)
print(x.insert(21))
print(x.delete(2))
print(x.find__smallest(2))

# DHT11 Program
# import sys
# import Adafruit_DHT
# import time

# while True:

#     humidity, temperature = Adafruit_DHT.read_retry(11, 4)

#     print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
#     time.sleep(1)

# t = int(input())
# while t:
#     C = int(input())
#     i = 1
#     while True:
#         if 2**i > C:
#             break
#         i += 1
#     x = 2**i
#     ans = 0
#     for i in range(x, 1, -1):
#         for j in range(x, i+1, -1):
#             if i^j == C:
#                 ans = max(ans, i*j)
#     print(ans)
#     t -= 1

# def solve(ratings, i):
#     b = 0
#     for j in range(len(ratings) - i):
#         x = sum(ratings[j:j+i])*min(ratings[j:j+i])
#         b = max(x, b)
#     return b

# def greatestValueDays(ratings):
#     ans = 0
#     n = len(ratings)
#     for i in range(1,n):
#         ans = max(ans, solve(ratings, i))
#         print(solve(ratings, i))
#     return ans

# ratings = [0,0,1,2,0,0]
# print(greatestValueDays(ratings))

def minimumTimeHire2021(drivers, batteries, p):
    ans = 2**31
    res = []
    for i in drivers:
        d = 10**31
        x = 10**31
        for j in batteries:
            if abs(j-i) <= d and abs(j-p) < x:
                d = abs(j-i)
                x = j
                print(d, x)
        
        ans = min(d + abs(x-p), ans)
        res.append(ans)

    print(res)
        
    return ans

d = [20, 100]
b = [60, 10, 40, 80]
p = 50
print(minimumTimeHire2021(d, b, p))


def coinChange(coins, amount):
    ans = 0
    if a <= 0: return 0
    i = len(coins)-1
    while amount > 0 and i > -1:
        if amount - coins[i] >= 0:
            ans += 1
            amount -= coins[i]
        else:
            i -= 1

    if amount > 0:
        return -1
    else:
        return ans

c = [1,2,5]
a = 11
print(coinChange(c, a))