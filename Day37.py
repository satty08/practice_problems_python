'''
Array Implementation of Tree
'''

tree = [None]*10

def set_root(key):
    if tree[0] != None:
        return
    else:
        tree[0] = key

def set_left(key, parent):
    if tree[parent] is None:
        return
    else:
        tree[(parent*2)+1] = key

def set_right(key, parent):
    if tree[parent] is None:
        return
    else:
        tree[(parent*2)+2] = key

def print_tree():
    for i in range(10):
        if tree[i] is not None:
            print(tree[i], end='')
        else:
            print('-', end='')

    
set_root('A')
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()

'''
Given a AVL tree and N values to be inserted in the tree. 
Write a function to insert a given value into the tree.
'''
class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def getHeight(root):
    if not root:
        return 0
    return root.height
    
def getBalance(root):
    if not root:
        return 0
        
    return getHeight(root.left) - getHeight(root.right)
    
def rotateRight(root):
    z = root.left
    t3 = z.right
    
    z.right = root
    root.left = t3
    
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    
    return z
    
def rotateLeft(z):
    y = z.right
    t2 = y.left
    
    y.left = z
    z.right = t2
    
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    
    return y

def insertToAVL(root, key):
    # add key to AVL (if it is not present already)
    # return root node
    if root == None:
        return Node(key)
        
    if key == root.data:
        return root
    
    if key < root.data:
        root.left = insertToAVL(root.left, key)
        
    else:
        root.right = insertToAVL(root.right, key)
        
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    
    balance = getBalance(root)
    
    if balance > 1 and key < root.left.data:
        return rotateRight(root)
        
    elif balance < -1 and key > root.right.data:
        return rotateLeft(root)
        
    elif balance > 1 and key > root.left.data:
        root.left = rotateLeft(root.left)
        return rotateRight(root)
        
    elif balance < -1 and key < root.right.data:
        root.right = rotateRight(root.right)
        return rotateLeft(root)
        
    return root