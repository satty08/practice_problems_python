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


def phazed_group_type(arr):
    d = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '0':10,
        'A':1,
        'J':11,
        'Q':12,
        'K':13
    }
    ans = []
    if arr is None:
        return []

    if len(arr) == 3:
        if arr[0][0] == arr[1][0] == arr[2][0]:
            ans.append(1)
    elif len(arr) == 7:
        for i in range(6):
            if arr[i][1] == arr[i+1][1]:
                ans.append(2)

    elif len(arr) == 4:
        count = 1
        for i in range(3):
            if arr[i][0] == arr[i+1][0]:
                count += 1
        h,d,s,c = 0,0,0,0
        for i in range(3):
            if arr[i][0] == 'h':
                h += 1
            elif arr[i][0] == 'd':
                d += 1

            elif arr[i][0] == 's':
                s += 1
            elif arr[i][0] == 'c':
                c += 1

            if s+c >= 4 or h+d >= 4:
                ans.append(5)
        if count >= 3:
            ans.append(3)

    elif len(arr) == 8:
        ans.append(4)
    res=0
    if len(arr) == 4:
        for i in arr:
            res += d[i[0]]

        if res==34:
            ans.append(6)

    return ans