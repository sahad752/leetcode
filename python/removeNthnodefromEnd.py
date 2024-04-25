class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def removenthfromend(self,head:ListNode,n:int)->ListNode:
        dummy = ListNode(0,head)
        left  = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n-=1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        print(dummy.next)
        return dummy.next

    def solution2(self,head,n):
        dummy = ListNode(next=head)
        right = dummy
        left = dummy

        while right and n >=0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next




if __name__ == "__main__":
    s = Solution()
    listnode = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,))))))
    answr = s.solution2(listnode,2)
    print(answr)