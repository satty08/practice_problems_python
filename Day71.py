'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root):
        
        def height(node):
            if not node: return 0
            return max(height(node.left), height(node.right)) + 1
        
        def dfs(node, d):
            if not node: return
            if d== h: self.ans += node.val
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        self.ans = 0
        h = height(root)
        dfs(root, 1)
        return self.ans