'''
Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.
'''

def ispar(x):
    # code here
    stack = []
    for i in x:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if not stack:
                return False
            curr = stack.pop()
            if i == ')' and curr != '(':
                return False
            elif i == ']' and curr != '[':
                return False
            elif i == '}' and curr != '{':
                return False
    if stack:
        return False
    return True