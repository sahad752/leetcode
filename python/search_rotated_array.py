from ast import List
import sys


class Solution:

    def search2(self, nums, target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0] == target else -1

        pivot_index = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def search(self, nums, target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0] == target else -1

        pivot_index = 0
        for i in range(len(nums)-1):
            if nums[0] > nums[i]:
                pivot_index = i+1
                break
        pivot = nums[pivot_index]
        first_array = nums[:pivot_index]
        second_array = nums[pivot_index:]
        if first_array and  target >= first_array[0] and target <= first_array[-1]:
            first_array_index = self.binary_search(first_array, target)
            return first_array_index if first_array_index != -1 else -1
        else:
            second_array_index =  self.binary_search(second_array, target)
            return len(first_array) + second_array_index if second_array_index != -1 else -1


    def binary_search(self, nums, target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    nums = [1,3]
    target = 0
    print(Solution().search2(nums, target))
    sys.exit()