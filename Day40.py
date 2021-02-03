'''
Given an array arr[] of N nodes representing preorder traversal of BST. The task is to print its postorder traversal.
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def constructTree(pre, size):
    inorder = sorted(pre)
    root = preToPost(pre, inorder)
    return root

def preToPost(pre, inorder):
    if len(inorder) == 0:
        return
    idx = inorder.index(pre[0])
    root = Node(pre[0])
    root.left = preToPost(pre[1:idx+1], inorder[0:idx])
    root.right = preToPost(pre[idx+1:], inorder[idx+1:])
    return root


pre = [40,30,32,35,80,90,100,120]
print(constructTree(pre, len(pre)))

import time

