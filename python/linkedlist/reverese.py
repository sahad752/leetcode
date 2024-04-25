
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self,list):
        dummy = result = ListNode(0)




if __name__ == "__main__":
    list1 = ListNode(1,ListNode(9,ListNode(21)))
    list2 = ListNode(4,ListNode(6,ListNode(7)))
    list3 = ListNode(1, ListNode(9, ListNode(21,ListNode(34,ListNode(12)))))
    solution = Solution()
    solution.reverse(list3)