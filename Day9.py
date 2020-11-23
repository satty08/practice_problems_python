def merge(arr1, arr2, n, m): 
    if n < m:
        for i in range(n):
            arr1.append(arr2[i])
        return arr1.sort()
    else:
        for i in range(m):
            arr2.append(arr1[i])
        return arr2.sort()
arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8]

print(merge(arr1, arr2, len(arr1), len(arr2)))