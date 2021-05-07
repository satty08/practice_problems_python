'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of 
every node never differ by more than 1.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
            
        def BST(low, high, nums, root):
            while low <= high:
                mid = (low+high)//2
                root = TreeNode(nums[mid])
                root.left = BST(low, mid-1, nums, root.left)
                root.right = BST(mid+1, high, nums, root.right)
                return root
        
        return BST(0, len(res)-1, res, None)

s = 'caba'
i, j = 0, len(s)
ans = ''
res = 0
flag = 0
while i < j:
    if s[i:j] == s[i:j][::-1]:
        res = max(res, j-i)
        ans = s[i:j]
    if flag == 0:
        i += 1
        flag = not flag
    else:
        j -= 1
    print(ans)
print(ans)