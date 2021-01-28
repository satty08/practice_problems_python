'''
Given a Binary Tree of size N, your task is to complete the function deletionBT(), that should delete a given node 
from the tree by making sure that tree shrinks from the bottom (the deleted node is replaced by bottommost and rightmost node).
'''

def deleteDeepestNode(root, temp):
    q = []
    q.append(root)
    while len(q):
        a = q.pop(0)
        if a is temp:
            return 
        if a.right:
            if a.right is temp:
                a.right = None
                return
            else:
                q.append(a.right)
        if a.left:
            if a.left is temp:
                a.left = None
                return
            else:
                q.append(a.left)

def deletionBT(root, key):
    '''
    root: root of tree
    key:  key to be deleted
    return: root after deleting 
    '''
    if root is None:
        return
    
    if root.left is None and root.right is None:
        if root.key == key:
            return None
        else:
            return root
            
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.data == key:
            key_Node = temp
            
        if temp.left:
            q.append(temp.left)
            
        if temp.right:
            q.append(temp.right)
            
    if key_Node:
        x = temp.data
        deleteDeepestNode(root, temp)
        key_Node.data = x
    return root

'''
Given a Binary Tree, find the In-Order Traversal of it.
'''
'''
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def inorderFun(root, res):
    if root == None:
        return
    inorderFun(root.left, res)
    res.append(root.data)
    inorderFun(root.right, res)

def InOrder(root):
    # code here
    res = []
    inorderFun(root, res)
    return res

'''
Given a binary tree, find its preorder traversal.
'''

def preorderFun(root, res):
    if root:
        res.append(root.data)
        preorderFun(root.left, res)
        preorderFun(root.right, res)

def preorder(root):
    '''
    :param root: root of the given tree.
    :return: a list containing pre order Traversal of the given tree.
    {
        class Node:
        def _init_(self,val):
            self.data = val
            self.left = None
            self.right = None
    }
    '''
    # code here
    res = []
    preorderFun(root, res)
    return res

'''
Given a binary tree of size N, you have to count number of nodes in it.
'''

def getSize(node):
    if node is None:
        return 0
    return getSize(node.left) + getSize(node.right) + 1

'''
Given a Binary Tree, find maximum and minimum elements in it.
'''

def findMax(root):
    '''
    :param root: root of the given tree.
    :return: max 
    
    '''
    #code here
    if root is None:
        return float('-inf')
        
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res
    
def findMin(root):
    '''
    :param root: root of the given tree.
    :return: min 
    
    '''
    #code here
    if root is None:
        return float('inf')
        
    res = root.data
    lres = findMin(root.left)
    rres = findMin(root.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res
