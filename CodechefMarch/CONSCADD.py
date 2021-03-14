def check(a, b, r, c):
    for i in range(r):
        for j in range(c):
            if a[i][j] != b[i][j]:
                return False
    return True

try:
    t = int(input())
    while t:
        R, C, X = map(int, input().split())
        arrA, arrB = [], []
        for i in range(R):
            a = list(map(int, input().split()))
            arrA.append(a)
        for i in range(R):
            a = list(map(int, input().split()))        
            arrB.append(a)

        if R<X and C<X:
            if check(arrA, arrB, R, C):
                print('Yes')
            else:
                print('No')
            continue
        
        elif(R<X):
            for i in range(R):
                for j in range(C-X+1):
                    if arrA[i][j] == arrB[i][j]:
                        continue
                    else:
                        diff = arrB[i][j] - arrA[i][j]
                        arrA[i][j] += diff
                        k = 1
                        while k < X:
                            arrA[i][j+k] += diff
                            k += 1
        
        elif(C < X):
            for i in range(C):
                for j in range(R-X+1):
                    if arrA[j][i] == arrB[j][i]:
                        continue
                    else:
                        diff = arrB[j][i] - arrA[j][i]
                        arrA[j][i] += diff
                        k = 1
                        while k < X:
                            arrA[j+k][i] += diff
                            k += 1
            
        elif(R >= X and C >= X):
            for i in range(R):
                for j in range(C-X+1):
                    if arrA[i][j] == arrB[i][j]:
                        continue
                    else:
                        diff = arrB[i][j] - arrA[i][j]
                        arrA[i][j] += diff
                        k = 1
                        while k < X:
                            arrA[i][j+k] += diff
                            k += 1
            for i in range(C):
                for j in range(R-X+1):
                    if arrA[j][i] == arrB[j][i]:
                        continue
                    else:
                        diff = arrB[j][i] - arrA[j][i]
                        arrA[j][i] += diff
                        k = 1
                        while k < X:
                            arrA[j+k][i] += diff
                            k += 1

        if check(arrA, arrB, R, C):
            print('Yes')
        else:
            print('No')
        t -= 1
except:
    pass