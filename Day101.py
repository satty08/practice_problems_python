'''
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively
from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:    
    def constructMaximumBinaryTree(self, nums):
        idx = nums.index(max(nums))
        left, right = nums[:idx], nums[idx+1:]
        root = TreeNode(nums[idx])
        if left:
            root.left = self.constructMaximumBinaryTree(left)
        if right:
            root.right = self.constructMaximumBinaryTree(right)
            
        return root

