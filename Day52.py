'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        ans = []
        if root == None:
            return ans
        
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            levelSum = 0
            
            x = len(q)
            for i in range(x):
                curr = q.pop()
                levelSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
            levelavg = levelSum/x
            ans.append(levelavg)
            
        return ans