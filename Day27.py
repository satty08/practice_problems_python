'''
Given a singly linked list of size N, and an integer K. You need to swap the Kth node from the beginning and Kth node from 
the end of the linked list. Swap the nodes through the links. Do not change the content of the nodes.
'''


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


def swapkthnode(head,num,k):
    # return head of new linked list
    #code here
    if num < k:
        return head
    if 2*k-1 == num:
        return head
    
    x = head
    x_prev = Node(None)
    for _ in range(k-1):
        x_prev = x
        x = x.next
        
    y = head
    y_prev = Node(None)
    for _ in range(num - k):
        y_prev = y
        y = y.next
        
    if x_prev is not None:
        x_prev.next = y
        
    if y_prev is not None:
        y_prev.next = x
        
    temp = x.next
    x.next = y.next
    y.next = temp

    if k == 1:
        head = y
    if k == num:
        head = x
        
    return head

'''
Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) 
and return head of the merged list.
Note: It is strongly recommended to do merging in-place using O(1) extra space.
'''

def sortedMerge(head_A, head_B):
    # code here
    dummy = Node(0)
    
    tail = dummy
    while True:
        if head_A is None:
            tail.next = head_B
            break
        if head_B is None:
            tail.next = head_A
            break
        
        if head_A.data <= head_B.data:
            tail.next = head_A
            head_A = head_A.next
            
        else:
            tail.next = head_B
            head_B = head_B.next
            
        tail = tail.next
        
    return dummy.next