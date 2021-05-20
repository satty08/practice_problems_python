'''
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, 
and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. 
Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls 
to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
'''
def minOperations(boxes):
    res, ans = [], []
    for i in range(len(boxes)):
        if boxes[i] == '1':
            res.append(i)
            
    for i in range(len(boxes)):
        sum_ = 0
        for j in res:
            sum_ += abs(j-i)
        ans.append(sum_)
        
    return ans

'''
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference 
to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        def inorder(o, c):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.ans = c
                inorder(o.right, c.right)
        
        inorder(original, cloned)
        return self.ans       