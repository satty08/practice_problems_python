'''
Your task is to implement  2 stacks in one array efficiently.
'''

'''
Function Arguments :
		@param  : a (auxilary array), 
		top1 and top2 are declared as two tops of stack.
		# initialized value of  tops of the two stacks
        top1 = -1
        top2 = 101
		@return : Accordingly.
'''
top1 = -1
top2 = 101

def pop1(a):
    #code here
    global top1
    if top1 == -1:
        return -1
    else:
        top1 -= 1
        return (a[top1+1])
def pop2(a):
    #code here
    global top2
    if top2 == 101:
        return -1
    else:
        top2 += 1
        return (a[top2-1])
def push1(a,x):
    #code here
    global top1
    top1 += 1
    a[top1] = x
    
def push2(a,x):
    #code here
    global top2
    top2 -= 1
    a[top2] = x