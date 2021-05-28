def evalRPN(tokens):
    stack = []
    op = '+-*/'
    res = 0
    stack.append(int(tokens[0]))
    i = 1
    while i < len(tokens):
        if tokens[i] not in op:
            stack.append(int(tokens[i]))
        else:
            a = stack.pop()
            b = stack.pop()
            if tokens[i] == '+':
                res = a+b
            elif tokens[i] == '-':
                res = b-a
            elif tokens[i] == '*':
                res = a*b
            elif tokens[i] == '/':
                res = int(b/a)
            stack.append(res)
            print(stack)
        i += 1
        
    return stack [-1]

token = ["4","-2","/","2","-3","-","-"]
print(evalRPN(token))

# n = int(input())
# res = '1'
# print(res)
# for i in range(1, n):
#     res += '*'*i + str(i+1)
#     print(res)


def equation(arr):
    res = []
    for i in arr:
        X, Y = i[0], i[1]
        count = 0
        modArr = [1] * (X+1)
        for j in range(2, X+1):
            a = Y%j
            count += modArr[a]
            for k in range(a, X+1, j):
                modArr[k] += 1
        res.append(count)
    return res

arr = [[1, 7], [7, 1], [98, 98], [12, 13], [34, 33], [89, 1000]]
print(equation(arr))