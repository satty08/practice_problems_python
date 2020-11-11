# def star(n):
#     for i in range(n):
#         print(' '*(n-i-1)+'*'*(2*i+1))
# star(9)

def fib(n):
    if n == 0:
        print(0)
    if n == 1:
        print(1)
    return fib(n-1) + fib(n-2)
fib(4)