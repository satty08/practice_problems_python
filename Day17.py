'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root 
of the tree, and every node has no left child and only one right child.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root):
        def dfs(node):
            l1, r2 = node, node
            
            if node.left:
                l1, l2 = dfs(node.left)
                l2.right = node
                
            if node.right:
                r1, r2 = dfs(node.right)
                node.right = r1
            
            node.left = None
            return (l1, r2)
        
        return dfs(root)[0]