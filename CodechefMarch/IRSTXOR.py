# try:
#     t = int(input())
#     while t:
#         C = int(input())
#         a = C
#         i = 1
#         while a>0:
#             a //= 2
#             i += 1
#         x = 2**i
#         ans = 0
#         i, j = 1, x-1
#         while i != j:
#             if i^j > C:
#                 i += 1

#             elif i^j < C:
#                 j -= 1
            
#             elif i^j == C:
#                 ans = max(ans, i*j)
#                 i += 1

#         print(ans)
#         t -= 1
# except:
#     pass

try:
    t = int(input())
    while t:
        c = int(input())
        x = c
        power, size = 0, 0
        while x > 0:
            if x%2 == 1:
                power += 1
            x = x//2
            size += 1

        a = [0]*size
        b = [0]*size
        v, x = size, c
        index = 0

        while x > 0:
            if x%2 == 0:
                a[index] = 1
                b[index] = 1
            else:
                if power == 1:
                    a[index] = 1
                    b[index] = 0
                else:
                    a[index] = 0
                    b[index] = 1

                power -= 1

            index += 1
            x = x//2

        aval, bval = 0, 0
        p = 1

        for i in range(v):
            aval += p*a[i]
            bval += p*b[i]

            p = p*2

        print(aval*bval)

        t -= 1
except:
    pass