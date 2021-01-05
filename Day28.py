'''
Given a Binary Tree of N edges. The task is to convert this to a Circular Doubly Linked List(CDLL) in-place. The left 
and right pointers in nodes are to be used as previous and next pointers respectively in converted CDLL. The order of 
nodes in CDLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) 
must be head node of the CDLL.
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def concatenate(leftList, rightList):
    if rightList == None:
        return leftList
        
    if leftList == None:
        return rightList
        
    leftLast = leftList.left
    rightLast = rightList.left
    
    leftLast.right = rightList
    rightList.left = leftLast
    
    leftList.left = rightLast
    
    rightLast.right = leftList
    
    return leftList

def bTreeToClist(root):
    #Your code here
    if root == None:
        return 
    
    leftList = bTreeToClist(root.left)
    rightList = bTreeToClist(root.right)
    
    root.left = root.right = root
    
    return concatenate(concatenate(leftList, root), rightList)
