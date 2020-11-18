# def star(n):
#     for i in range(n):
#         print(' '*(n-i-1)+'*'*(2*i+1))
# star(9)

def main(l):
    l1 = []
    l2 = []
    for i in range(len(l)):
        if i < len(l)//2:
            l1.append(l[i])
        else:
            l2.append(l[i])
    l1.remove(min(l1))
    l2.remove(min(l2))
    l2 = l2[::-1]
    sum = 0
    for i in range(len(l1)):
        sum += l1[i]*l2[i]
    return sum

l = [1, 9, 2, 3, 0, 6, 7, 8]
print(main(l))