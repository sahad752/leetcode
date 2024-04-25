class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_node_fromEnd(self,list1,n):


        counter = 0
        list2 = list1
        while list2:
            counter+=1
            list2 = list2.next

        dummy = ListNode(0)
        dummy.next = list1
        nth_node = counter-n+1
        counter = 0
        list1 = dummy
        while list1:
            counter+=1
            if counter == nth_node:
                list1.next = list1.next.next
                pass
            list1 = list1.next
        return dummy.next
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        while n>0:
            fast= fast.next
            n-=1
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    list1 = ListNode(1,ListNode(9,ListNode(21)))
    list2 = ListNode(4,ListNode(6,ListNode(7)))
    list3 = ListNode(1, ListNode(9, ListNode(21,ListNode(34,ListNode(12)))))
    solution = Solution()
    solution.removeNthFromEnd(list3,1)