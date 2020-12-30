'''
Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the 
position just after pth node in the doubly linked list.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def addNode(head, p, data):
    # Code here
    temp = head
    x = Node(data)
        
    while p != 0:
        temp = temp.next
        p -= 1
    
    x.prev = temp
    x.next = temp.next
    if temp.next is not None:
        temp.next.prev = x
    temp.next = x
    return head

'''
Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.
'''

def deleteNode(head, x):
    # Code here
    if head == None:
        return None
    elif head.next == None:
        return None
    else:
        curr = head
        while curr.next != None and x > 1:
            x -= 1
            curr = curr.next
        if x < 2:
            if curr.prev != None:
                curr.prev.next = curr.next
            if curr.next != None:
                curr.next.prev = curr.prev
    return head

'''
Given a doubly linked list of n elements. The task is to reverse the doubly linked list.
'''

def reverseDLL(head):
    #return head after reversing
    # curr = head
    # res = head
    # while curr.next is not None:
    #     curr = curr.next
    # while curr != res:
    #     x = res.data
    #     res.data = curr.data
    #     curr.data = x
        
    #     curr = curr.prev
    #     res = res.next
    # return head
    p1, p2 = None, head
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p2.prev = p3
        p1 = p2
        p2 = p3
    return p1