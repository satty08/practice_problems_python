'''
Given a Binary Tree, write a function to populate next pointer for all nodes. The next pointer for every node 
should be set to point to inorder successor.
'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        self.next=None

def populateNext(root):
    
    '''
    don't print anything
    just populate tree next pointer
    '''
    #code here
    arr = [None]
    populate(root, arr)
    
def populate(root, arr):
    if root == None:
        return None
        
    populate(root.left, arr)
    
    if arr[0] != None:
        arr[0].next = root
        
    arr[0] = root
    populate(root.right, arr)

'''
Given a BST, and a reference to a Node x in the BST. Find the Inorder Successor of the given node in the BST.
'''

def inorderSuccessor(root, x):
    # Code here
    if not root:
        return None
        
    y = Node(None)
    
    if root.data <= x.data:
        y = inorderSuccessor(root.right, x)
        
    elif root.data > x.data:
        y = inorderSuccessor(root.left, x)
        if y == None:
            y = root
            
    return y