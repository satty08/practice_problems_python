m = 6
n = 3
count = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if (m%i)%j == (m%j)%i:
            print(i, j, m)
            count+=1

print(count)


def gcd(x, y):
    while(y):
      x, y = y, x % y
  
    return x
try:
    t = int(input())
    mod = 10**9+7
    while t:
        k = int(input())
        res = 0
        for j in range(1, 2*k+1):
            res += gcd(k+j*j, k+(j+1)*(j+1))
            
        res = res%mod
        print(res)
        t -= 1
except:
    pass