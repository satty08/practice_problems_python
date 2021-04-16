'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes 
greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

def partition(head, x):
    bef = bef_head = ListNode(0)
    aft = aft_head = ListNode(0)
        
    while head:
        if head.val < x:
            bef.next = head
            bef = bef.next
                
        else:
            aft.next = head
            aft = aft.next
                
        head = head.next
            
    aft.next = None
        
    bef.next = aft_head.next
        
    return bef_head.next

'''
Given two strings a and b, return true if you can swap two letters in a so the result is equal to b, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters 
at a[i] and a[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
'''

def buddyStrings(a, b):
    if len(a) != len(b): return False
    
    if a == b:
        s = set()
        for i in a:
            if i in s:
                return True
            s.add(i)
            
        return False
    
    else:
        
        pairs = []
        for i, j in zip(a, b):
            if i != j:
                pairs.append((i, j))
                
            if len(pairs) >= 3: return False
            
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

'''
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
Return the operations to build the target array. You are guaranteed that the answer is unique.
'''

def buildArray(target, n):
    res = []
    i = 1
    x = len(target)
    while x > 0:
        if i not in target:
            res.append('Push')
            res.append('Pop')
            
        else:
            res.append('Push')
            x -= 1
            
        i += 1
            
    return res