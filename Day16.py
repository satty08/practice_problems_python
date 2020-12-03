'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # curr = self.head
        # lenList = 0
        # while curr:
        #     curr = curr.next
        #     lenList += 1
        # x = random.random()
        # v = lenList*x
        # temp = self.head
        # while v:
        #     temp = temp.next
        #     v -= 1
        # return temp
        k = 1
        curr = self.head
        while curr is not None:
            if random.randint(1, k) <= 1:
                res = curr.val
            curr = curr.next
            k += 1
        return res
        

# Your Solution object will be instantiated and called as such: