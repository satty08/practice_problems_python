def smallestnum (N):
    # code here 
    s = str(N)
    res = []
    for i in s:
        res.append(int(i))
            
    res.sort()
    ans = ''
    for i in range(len(res)):
        if res[i] != 0 and i == 0:
            break
        elif res[i] != 0:
            res[0] = res[i]
            res[i] = 0
            break
            
    for i in res:
        ans += str(i)
    return int(ans)

n = 3472920
print(smallestnum(n))