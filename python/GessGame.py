

class Solution:

    def guess(self,num) :
        if num == 7:
            return 0
        elif num < 7:
            return 1
        else :
            return -1

    def guessNumber(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if self.guess(mid) == 1:
                lo = mid+1
            else:
                hi = mid
        return lo

solution = Solution()
# solution.guessNumber(6)

print(solution.guessNumber(10))