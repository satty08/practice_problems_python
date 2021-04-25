def solve(s, w):
    flag = 0
    for i in range(len(w)):
        b = set(w[i])
        for j in b:
            if w[i].count(j) > s.count(j):
                flag = 0
                break
            else:
                flag = 1

        if flag == 1:
            break
    return flag

s = "atyabeksjncekncncsi"
w = ['byte', 'satyam', 'yayatika']
print(solve(s, w))

arr = ['d', 'aad', 'aaad']
print(chr(97+28))

def alphabet(arr, k):
    k = k%26
    print(k)
    s = chr(96+k)
    res = []
    for i in arr:
        if i == 1:
            res.append(s)
        else:
            res.append(chr(97)*(i-1)+s)

    return sorted(res)

arr = [2]
k = 10000000
print(alphabet(arr, k))