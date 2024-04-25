# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        # Create a new linked list to store the result
        curr = ListNode()
        result = curr
        carry = 0

        while l1 or l2:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            curr.val = total % 10

            carry = total // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2:
                curr.next = ListNode()
                curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return result

sd = Solution()
l1 = ListNode(1,ListNode(2,ListNode(5)))
l2 = ListNode(2,ListNode(9))

sd.addTwoNumbers(l1,l2)