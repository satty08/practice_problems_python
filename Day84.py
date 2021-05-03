def twoSum(nums, target):
    i, j = 0, len(nums)-1
    nums.sort()
    while i <= j:
        print(i, j)
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        
    return []

arr = [3,2,4]
print(twoSum(arr, 6))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = ListNode(0)
        head = res
        
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            carry, ans = divmod(x+y+carry, 10)
            head.next = ListNode(ans)
            head = head.next
            
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            
        return res.next