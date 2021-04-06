'''
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.
'''
# Time Limit Exceeded
# def isIdealPermutation(A):
#     Global = 0
#     local = 0
#     for i in range(len(A)):
#         for j in range(i+1, len(A)):
#             if A[i] > A[j]:
#                 Global += 1
                    
#     for i in range(len(A)-1):
#         if A[i] > A[i+1]:
#             local += 1
                
#     return Global == local

# Optimal Solution
def isIdealPermutation(A):
    for i in range(len(A)):
        if i - A[i] > 1 or i - A[i] < -1: return False
    return True

s = '1001011'
i = 0
while True:
    x = bin(i)[2:]
    print(x)
    if (x not in s) and (x not in s[::-1]):
        break
    i += 1

print(i)

print(bin(12)[2:])


def Solve(n, s):
    while True:
        x = bin(n)[2:]
        a, b = 0, 0
        while a < len(x) and b < len(s):
            if x[a] == s[b]:
                a += 1
            b += 1
        if a == len(x):
            n += 1
            continue
        else:
            break
    return x

try:
    t = int(input())
    while t:
        s = input()
        print(Solve(0, s))
        
        t -= 1
except:
    pass

def avoidFlood(rains):
    st = []
    res = []
    for i in rains:
        if i != 0 and i not in st:
            res.append(-1)
            st.append(i)
        elif i != 0 and i in st:
            return []
        elif i == 0 and len(st) > 0:
            x = st.pop()
            res.append(x)
        elif i == 0 and len(st) == 0:
            res.append(1)
                
    return res

rain = [10, 20,20]
print(avoidFlood(rain))