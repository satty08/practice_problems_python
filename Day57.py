'''
Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  
For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is 
also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.
'''

def search(n):
    if n in [0,1]:
        return str(n)
    elif n%2 == 0:
        return '0'+ search(n//-2)

    else:
        return '1'+ search((n-1)//-2)

def addNegabinary(arr1, arr2):
        num = 0
        for i in range(len(arr1)):
            num += arr1[i]*(-2)**(len(arr1)-i-1)

        for i in range(len(arr2)):
            num += arr2[i]*(-2)**(len(arr2)-i-1)
        print(num)
        res = search(num)
        q = [int(x) for x in res]
        q.reverse()
        return q

a1 = [0]
a2 = [0]

print(addNegabinary(a1, a2))

'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, 
each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
'''

def isAdditiveNumber(self, num: str) -> bool:
        
    for i in range(1, (len(num)//2) + 1):
        if num[0] != "0" or i == 1:
            for j in range(1, (len(num)//2)+1):
                if num[i] != "0" or j == 1:
                    n3off = i+j
                    n1, n2, n3 = num[:i], num[i:n3off], num[n3off:]
                    while n3.startswith(str(int(n1)+ int(n2))):
                        n1, n2 = n2, str(int(n1)+int(n2))
                        n3off += len(n2)
                        n3 = num[n3off:]
                        if not n3: return True
                            
    return False


'''
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.
'''

def advantageCount(self, A, B):
    sortA = sorted(A)
    sortB = sorted(B)
        
    assign = {b: [] for b in B}
    remain = []
        
    j = 0
        
    for a in sortA:
        if a > sortB[j]:
            assign[sortB[j]].append(a)
            j += 1
        else:
            remain.append(a)
                
    return [assign[b].pop() if assign[b] else remain.pop() for b in B]