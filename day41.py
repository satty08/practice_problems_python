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

'''
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children 
is separated by the null value (See examples).
'''

# First Approach
class Solution1:
    def __init__(self):
        self.l = []
        
    def postorder(self, root):
        if root is None:
            return None
        
        for i in root.children:
            self.postorder(i)
            
        self.l.append(root.val)
        
        return self.l

# Second Approach
class Solution2:
    def postorder(self, root):
        st = [root]
        l = []
        
        while st:
            node = st.pop()
            
            if node:
                l.insert(0, node.val)
                if node.children:
                    for i in node.children:
                        st.append(i)
                        
        
        return l

# Third Approach

class Solution3:
    def postorder(self, root):
        st = [root]
        l = []
        
        while st:
            node = st.pop()
            
            if node:
                l.append(node.val)
                if node.children:
                    for i in node.children:
                        st.append(i)
        l.reverse()
        
        return l