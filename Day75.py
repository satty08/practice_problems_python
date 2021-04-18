# mat = [
#     [0,1,0],
#     [1,1,1],
#     [0,1,0]
# ]
# t = 0
# res = 0
# x, y = len(mat), len(mat[0])
# for i in range(x):
#     for j in range(y):
#         print(sum(mat[0:i][0:j]), i)
# print(res)

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

    
details = [
    ['Harry Kane', 'Tottenham', 19, 12],
    ['Mohd. Salah', 'Liverpol', 19, 11],
    ['Bruno Fernandes', 'Man Utd', 16, 12],
    ['Patrick Bamford', 'Leeds Utd', 14, 13],
    ['Jamie Vardy', 'Leicester', 12, 13]
]

avg = {}

for i in range(len(details)):
    x = round(details[i][2]/details[i][3], 3)
    avg[details[i][0]] = x

print(avg)