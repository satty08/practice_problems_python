'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

def merge(intervals):
    ans = []
    intervals.sort()
    ans.append(intervals[0])
    for i in range(1, len(intervals)):
        if ans[-1][1] >= intervals[i][0]:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
            
        else:
            ans.append(intervals[i])
            
    return ans


def generateMatrix(n):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    ans[0][0] = 1
    i, j = 0, 0
    count = 2
    while count <= (n**2):
        while j < n-1 and ans[i][j+1] == 0:
            ans[i][j+1] = count
            j += 1
            count+=1
            
        while i < n-1 and ans[i+1][j] == 0:
            ans[i+1][j] = count
            i+=1
            count+=1
            
        while j > 0 and ans[i][j-1] == 0:
            ans[i][j-1] = count
            j-=1
            count+=1
        
        while i > 0 and ans[i-1][j] == 0:
            ans[i-1][j] = count
            i-=1
            count+=1
        
        
    return ans

print(generateMatrix(3))