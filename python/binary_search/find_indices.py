def targetIndices(nums, target: int):
    nums.sort()
    l = 0
    r = len(nums)-1
    while l<=r:
        m = (r+l)//2
        if target <= nums[m]:
            r = m-1
        else:
            l = m+1
    return l

result  = targetIndices([1,2,5,2,3],3)
print(result)