class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        max1 = 0
        for i in range(k):
            max1 = nums.pop()
        return max1


    def findKthLargest(self, nums, k: int) -> int:
        import heapq
        nums = [-x for x in nums]
        heapq.heapify(nums)
        max1 = 0
        for i in range(k):
            max1 = -heapq.heappop(nums)

        return max1