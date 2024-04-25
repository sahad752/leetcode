class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        cnt = [0] * (n + 1)
        for it in trust:
            cnt[it[1]] += 1
            cnt[it[0]] -= 1
        for i in range(1, n + 1):
            if cnt[i] == n - 1:
                return i
        return -1



result  = Solution().findJudge(3,[[1,3],[2,3],[3,1]])