'''
Given an array(0-based indexing), you have to find the max sum of i*A[i] where A[i] is the element at index i in the array. 
The only operation allowed is to rotate(clock-wise or counter clock-wise) the array any number of times.
'''
# Naive Approach
def rotate(arr):
    n = len(arr)
    temp = arr[0]
    for j in range(n-1):
        arr[j] = arr[j+1]
    arr[n-1] = temp
    return arr

def max_sum(a,n):
    #code here
    maxsum = 0
    for _ in range(n):
        currsum = 0
        rotate(a)
        for j in range(n):
            currsum += j*a[j]
        maxsum = max(maxsum, currsum)
    return maxsum

arr = [1,2,3,4]

# Efficient Approach
def max_sum1(a,n):
    #code here
    curr_sum = 0
    
    for i in range(n):
        curr_sum += a[i]
        
    res = 0
    for i in range(n):
        res += i*a[i]
        
    max_val = res
    
    for i in range(1, n):
        next_val = (res - (curr_sum - a[i-1]) + a[i-1]*(n-1))
        
        res = next_val
        
        max_val = max(max_val, next_val)
        
    return max_val


