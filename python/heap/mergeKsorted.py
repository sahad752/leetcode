import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self,lists):
        head = root = ListNode()
        heap = []
        heapq.heapify(heap)
        for listn in lists:
            curr = listn
            while curr:
                heapq.heappush(heap,curr.val)
                curr = curr.next
        while heap:
            head.next = ListNode(heapq.heappop(heap))
            head = head.next
        return root.next

if __name__ == "__main__":
    list2 = ListNode(1,ListNode(2,ListNode(5)))
    list1 = ListNode(6,ListNode(3,ListNode(9)))
    List3 = ListNode(10,ListNode(34,ListNode(89)))
    sol = Solution()
    result = sol.merge([list1,list2,List3])
    print(result)