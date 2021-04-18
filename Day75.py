mat = [
    [0,1,0],
    [1,1,1],
    [0,1,0]
]
t = 0
res = 0
x, y = len(mat), len(mat[0])
for i in range(x):
    for j in range(y):
        print(sum(mat[0:i][0:j]), i)
print(res)

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
            
        res.pop(len(res)-n)
        root = ListNode(0)
        temp = root
        for i in range(len(res)):
            temp.next = ListNode(res[i])
            temp = temp.next
            
        return root.next