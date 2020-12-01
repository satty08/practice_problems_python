def checksum(a, b):   
    res = 0
    for i in range(a, b+1):
        for j in range(i, b+1):
            if (i+j)%8 == 0 or (i+j)%14 == 0:
                if i == j:
                    res += 1
                else:
                    res += 2
                print(i, j)
    return res

print(checksum(4, 8))