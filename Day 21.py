def rotateImage(a):
    n = len(a)
    for i in range(n):
        for j in range(i, n):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp
            
    for i in range(n):
        for j in range(n//2):
            temp = a[i][j]
            a[i][j] = a[i][n-1-j]
            a[i][n-1-j]=temp
    return a

a = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateImage(a))