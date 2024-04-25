
class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow :
                return True
        return False

    def rotate(self,head,k):
        if not head:
            return head

        length , tail = 1 , head

        while tail.next:
            tail = tail.next
            length +=1

        k = k % length
        curr = head
        for i in range(length - k-1):
            curr = curr.next

        newHead = curr.next
        curr.next = None
        tail.next = head

        printDummy = newHead
        while printDummy:
            print(printDummy.val)
            printDummy = printDummy.next
        print(newHead)

if __name__ == "__main__":
    list1 = ListNode(2,ListNode(0,ListNode(-4)))
    s = Solution()
    s.hasCycle(list1)