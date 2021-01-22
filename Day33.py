'''
Infix to Postfix
'''

def intopost(exp):
    x = ''
    s = []
    for i in exp:
        if i.isalnum():
            x += i
        elif i in '+-':
            s.append(i)
        elif i in '*/':
            s.append(i)
        elif i == '(':
            s.append(i)
        elif i == ')':
            a = ''
            while a != '(' or len(s) != 0:
                a = s.pop()
                if a == '(':
                    break
                x += a
    return x

exp = '((a+d-c)+(s/a*b))'
print(intopost(exp))

'''
Prefix to Postfix
'''

def pretopost(exp):
    exp = exp[::-1]
    operator = set(['+', '-', '*', '/', '^'])
    s = []
    for i in exp:
        if i in operator:
            a = s.pop()
            b = s.pop()
            temp = a + b + i
            s.append(temp)
        else:
            s.append(i)
    print(*s)
    return

exp = '+-abc'
print(pretopost(exp))