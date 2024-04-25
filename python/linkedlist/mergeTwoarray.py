
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self,list1,list2):
        dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                dummy.val = list1.val
                list1 = list1.next
            else:
                dummy.val = list2.val
                list2 = list2.next
            dummy.next = ListNode()

        return dummy.next


    def swapPairs(self, head):
        dummy = curr = ListNode(0)
        curr.next = head
        dummy2 = ListNode(0)
        dummy3 = dummy2

        while curr:
            curr1 = curr.next.val
            curr2 = curr.next.next.val
            dummy2.next = ListNode(curr2,ListNode(curr1))
            curr = curr.next.next
            dummy2 = dummy2.next



if __name__ == "__main__":
    list1 = ListNode(1,ListNode(9,ListNode(21)))
    list2 = ListNode(4,ListNode(6,ListNode(7)))
    list3 = ListNode(1, ListNode(9, ListNode(21,ListNode(34,ListNode(12)))))
    solution = Solution()
    solution.swapPairs(list3)
    solution.merge(list1,list2)