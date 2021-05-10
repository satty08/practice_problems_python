def isPossible(target):
    res = [1]*(len(target))
    target.sort()
    i = 0
    while i < len(target):
        if sum(res) < target[i]:
            idx = res.index(min(res))
            res[idx] = sum(res)

        elif sum(res) == target[i]:
            i += 1
            idx = res.index(min(res))
            res[idx] = sum(res)
        else:
            return False
        print(res)
    return res.sort() == target.sort()

arr = [1,1,1,2]
print(isPossible(arr))

def gcd(x, y):
    while(y):
      x, y = y, x % y
  
    return x
try:
    t = int(input())
    arr = []
    mod = 10**9+7
    while t:
        k = int(input())
        res = 0
        if len(arr) >= 2*k+1:
            res = sum(arr[2*k])
        elif len(arr) == 0:
            for j in range(1, 2*k+1):
                res += gcd(k+j*j, k+(j+1)*(j+1))
                arr.append(res)
        elif 0 < len(arr) < k:
            res = sum(arr)
            for j in range(len(arr)+1, 2*k+1):
                res += gcd(k+j*j, k+(j+1)*(j+1))
                arr.append(res)
                
        res = res%mod
        print(res)
        print(arr)
        t -= 1
except:
    pass