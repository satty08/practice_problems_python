'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''

def searchMatrix(self, matrix, target):
    for i in range(len(matrix)):
        if target in matrix[i]:
            return True
    return False

'''
You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a 
binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then 
this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer. 
'''

def sumRootToLeaf(self, root):
    ans = 0
    s = [(root, 0)]
        
    while s:
        root, curr = s.pop()
        if root is not None:
            curr = (curr << 1) | root.val
            if root.left is None and root.right is None:
                ans += curr
            else:
                s.append((root.right, curr))
                s.append((root.left, curr))
                    
    return ans

'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
'''

def isUnivalTree(self, root):
    left_unival = root.left == None or root.left.val == root.val and self.isUnivalTree(root.left)
    right_unival = root.right == None or root.right.val == root.val and self.isUnivalTree(root.right)
    return left_unival and right_unival