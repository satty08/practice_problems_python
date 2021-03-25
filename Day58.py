'''
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
'''
import collections
def distanceK(self, root, target, K):
    def dfs(node, parent = None):
        if node:
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
                
    dfs(root)
            
    queue = collections.deque([(target, 0)])
    seen = {target}
            
    while queue:
        if queue[0][1] == K:
            return [node.val for node, d in queue]
                
        node, d = queue.popleft()
        for nei in (node.left, node.right, node.parent):
            if nei and nei not in seen:
                seen.add(nei)
                queue.append((nei, d+1))
                        
    return []


'''
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the 
answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
'''
class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


class Solution:
    memo = {0: [], 1: [TreeNode(0)]}
    def allPossibleFBT(self, n):
        if n not in Solution.memo:
            ans = []
            for x in range(n):
                y = n-x-1
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[n] = ans
            
        return Solution.memo[n]