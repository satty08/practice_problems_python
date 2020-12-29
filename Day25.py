'''
Given a linked list of N nodes. The task is to check if the the linked list has a loop. Linked list can contain self loop.
Your task is to detect if any loop is present 
	in the given linked list.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: True or False (boolean)

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

def detectLoop(head):
    #code here
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

'''
Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.
'''

def isPalindrome(head):
    #code here
    res = []
    temp = head
    while temp:
        res.append(temp.data)
        temp = temp.next
    if res == res[::-1]:
        return 1
    else:
        return 0


'''
Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the 
given list (if exists).
Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way.
'''

def removeDuplicates(head):
    #code here
    ptr = head
    temp = head
    if ptr == None:
        return
    
    while ptr.next != None:
        if ptr.data == ptr.next.data:
            temp = ptr.next.next
            ptr.next = None
            ptr.next = temp
        else:
            ptr = ptr.next
    return head