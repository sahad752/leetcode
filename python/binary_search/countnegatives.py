class Solution:
    def countNegatives(self, grid) -> int:
        count = 0

        for row in grid:
            l = 0
            r = len(row) - 1
            while l <= r:
                m = (l + r) // 2

                if row[m] < 0:
                    r = m - 1
                else:
                    l = m + 1

            count += len(row) - l
        return count

result = Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])