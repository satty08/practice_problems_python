'''
Given a binary tree, find its level order traversal.
Level order traversal of a tree is breadth-first traversal for the tree.
'''

def levelOrder( root ):
    # Code here
    if root is None:
        return
    queue = []
    
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].data, end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return queue

'''
Given a Binary Search Tree and a node value X. Delete the node with the given value X from the BST. 
If no node with value x exists, then do not make any change. 
'''

def minValueNode(node):
    curr = node
    
    while curr.left is not None:
        curr = curr.left
        
    return curr

def deleteNode(root, X):
    # code here.
    if root is None:
        return root
        
    if X < root.data:
        root.left = deleteNode(root.left, X)
        
    elif X > root.data:
        root.right = deleteNode(root.right, X)
        
    else:
        
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
            
        temp = minValueNode(root.right)
        
        root.data = temp.data
        
        root.right = deleteNode(root.right, temp.data)
        
    return root