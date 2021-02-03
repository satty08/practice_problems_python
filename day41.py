'''
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        self.res = 0
        
        if root is None:
            return 0
        
        def sumRoot(root):
            if root:
                if root.val >= low and root.val <= high:
                    self.res += root.val

                if root.left:
                    sumRoot(root.left)

                if root.right:
                    sumRoot(root.right)

        sumRoot(root)
        return self.res