def minimumTotal(triangle):
    res = triangle[0][0]
    i = 0
    for j in range(1, len(triangle)):
        x = min(triangle[j][i], triangle[j][i+1])
        i = triangle[j].index(x)
        res += x
        
    return res

print(minimumTotal([[-1],[2,3],[1,-1,-3]]))

print(min(-40, -5))