class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        dp = [1]*n
        nxt = [i for i in range(n)]
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if nums[j]%nums[i]==0:
                    if 1+dp[j]>dp[i]:
                        dp[i] = dp[j]+1
                        nxt[i] = j
        idx = dp.index(max(dp))
        ans = []
        while idx!=nxt[idx]:
            ans.append(nums[idx])
            idx = nxt[idx]


        return ans+[nums[idx]]

s = Solution()
print(s.largestDivisibleSubset([1,2,4,8]))
print(s.largestDivisibleSubset([1,2,3,4,5]))
