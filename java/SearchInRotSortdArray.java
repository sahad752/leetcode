class Solution {
    public int search(int[] nums, int target) {
        int hi = nums.length-1;
        int lo = 0;
        int mid ;
        while(lo<=hi)
        {
            mid = (lo+hi)/2;
            if(nums[mid]==target)
            {
                 return mid;

            }
            if(nums[mid]>=nums[lo])
            {
                if(target<=nums[mid]&&target>=nums[lo]){
                    hi = mid-1;
                }else
                {
                    lo = mid+1;
                }
            }else{
                if(target>=nums[mid]&&target<=nums[hi])
                {
                    lo = mid+1;
                }else
                {
                    hi = mid-1;
                }
            }
        }
        return -1;
    }
}
