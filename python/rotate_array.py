
def rotate1( nums, k):
        k = k % len(nums)


        second_part = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = second_part[:]


def rotate(nums,k):
    k = k %len(nums)
    l,r = 0,len(nums)-1

    while l <r :
        nums[l],nums[r] = nums[r],nums[l]
        l=l+1
        r = r -1
    l,r = 0,k-1
    while l<r :
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1
    l,r = k,len(nums)-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1



if __name__ == "__main__":
    arary = [1,2,3,4,5,6,7,8]
    k = 3
    res = rotate1(arary,k)
    print(res)