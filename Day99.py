'''
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, 
if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of 
them. It is guaranteed that there will be at least one valid solution for the given input.
'''
def groupThePeople(groupSizes):
    res = []
    ans = {}
    
    for i in range(len(groupSizes)):
        if groupSizes[i] not in ans:
            ans[groupSizes[i]] = [i]
        else:
            ans[groupSizes[i]].append(i)
            
    for key, value in ans.items():
        if key != len(value):
            for i in range(0, len(value), key):
                res.append(value[i:i+key])
        else:
            res.append(value)
    return res

'''
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
(A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode):
        self.sum_ = 0
        
        def dfs(root, parent, gParent):
            if root == None:
                return 0
            if gParent != None and gParent.val%2 == 0:
                self.sum_ += root.val
                
            dfs(root.left, root, parent)
            dfs(root.right, root, parent)
        
        if root == None:
            return 0
        dfs(root, None, None)
        return self.sum_

'''
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is 
one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes 
ui and vi. Return the center of the given star graph.
'''

def findCenter(edges):
    ans = {}
    for i in edges:
        x, y = i[0], i[1]
        if x in ans: 
            ans[x] += 1
        else: 
            ans[x] = 1
        
        if y in ans: 
            ans[y] += 1
        else: 
            ans[y] = 1
            
        if ans[x] == 2:
            return x
        elif ans[y] == 2:
            return y               


def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 > 0:
            enable_print = 1
        if enable_print >= 1:
            print(N % 10, end="")
        N = N // 10

print(solution(1000000000))