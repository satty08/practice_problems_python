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

n = int(input())
res = '1'
print(res)
for i in range(1, n):
    res += '*'*i + str(i+1)
    print(res)