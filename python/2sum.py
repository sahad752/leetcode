class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index, num in enumerate(nums):
            # a + b = target -> a = target - b
            another = target - num
            if another in seen:
                return [seen[another], index]
            seen[num] = index


nums = [4,3,1,1,5,6,3,2]
target = 6
test = Solution()
print(test.twoSum(nums,target))