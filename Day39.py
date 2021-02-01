'''
Given a binary tree, check if the tree can be folded or not. A tree can be folded if left and right subtrees of 
the tree are structure wise same. An empty tree is considered as foldable.
'''
class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None

def mirror(node):
    if node is None:
        return
    
    else:
        temp = Node
        
        mirror(node.left)
        mirror(node.right)
        
        temp = node.left
        node.left = node.right
        node.right = temp
        
def isSame(nodeA, nodeB):
    if nodeA == None and nodeB == None:
        return True
        
    if nodeA != None and nodeB != None and isSame(nodeA.left, nodeB.left) and isSame(nodeA.right, nodeB.right):
        return True
        
    return False

def IsFoldable(root):
    # code here
    if root is None:
        return True
        
    mirror(root.left)
    
    res = isSame(root.left, root.right)
    
    mirror(root.left)
    
    return res

'''
Given a full binary expression tree consisting of basic binary operators (+ , – ,*, /) and some integers, 
Your task is to evaluate the expression tree.
'''

def evalTree(root):
    # Code here
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return int(root.data)
        
    left_sum = evalTree(root.left)
    right_sum = evalTree(root.right)
    
    if root.data == '+':
        return int(left_sum + right_sum)
    elif root.data == '-':
        return int(left_sum - right_sum)
    elif root.data == '*':
        return int(left_sum * right_sum)
    elif root.data == '/':
        return int(left_sum / right_sum)

'''
Given an array of size N, find the number of distinct pairs {a[i], a[j]} (i != j) in the array with their sum greater than 0.
'''

def ValidPair(self, a, n): 
    # Your code goes here
    low = 0
    high = n-1
    a.sort()
    res = 0
    while low < high:
        if a[low] + a[high] > 0:
            res += high - low
            high -= 1
        else:
            low += 1
            
    return res