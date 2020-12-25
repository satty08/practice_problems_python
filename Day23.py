'''
Given an unsorted array arr[] of size N, rotate it by D elements (clockwise). 
'''

t = int(input())
while t:
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    res = ''
    while D > 0:
        temp = arr[0]
        for i in range(N-1):
            arr[i] = arr[i+1]
        arr[N-1] = temp
        D -= 1
    for i in range(N):
        arr[i] = str(arr[i])
    res = " ".join(arr)
    print(res)
    t -= 1