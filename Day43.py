'''
Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level.
'''

def reverseLevelOrder(root):
    # code here
    h = height(root)
    res = []
    for i in reversed(range(1, h+1)):
        printReverseLevelOrder(root, i, res)
        
    return res
        
def printReverseLevelOrder(root, i, res):
    if root is None:
        return
    
    if i == 1:
        res.append(root.data)
        
    if i > 1:
        printReverseLevelOrder(root.left, i-1, res)
        printReverseLevelOrder(root.right, i-1, res)
        
def height(root):
    if root is None:
        return 0
        
    lheight = height(root.left)
    rheight = height(root.right)
    
    if lheight > rheight:
        return lheight + 1
        
    else:
        return rheight + 1

'''
Given a complete binary tree, reverse the nodes present at alternate levels.
'''

def preorder(root1, root2, lvl):
    if root1 == None or root2 == None:
        return
    
    if lvl%2 == 0:
        t = root1.data
        root1.data = root2.data
        root2.data = t
        
    preorder(root1.left, root2.right, lvl+1)
    preorder(root1.right, root2.left, lvl+1)

def reverseAlternate(root):
    '''
    :param root: root of given tree.
    '''
    # code here
    preorder(root.left, root.right, 0)