from pickletools import long1
import re


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        max_len = 0
        n= len(s)
        DP = [[0] * n for _ in range(n)]


        for i in range(n):
            DP[i][i] = 1
            max_len = 1
            ans = s[i]

        for i in range(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = 1
                max_len = 2
                ans = s[i:i+2]

        for j in range(n):
            for i in range(0,j-1):
                if s[i]==s[j] and DP[i+1][j-1] == 1:
                    DP[i][j] = 1
                    if max_len < j-i+1:
                        max_len = j-i+1
                        ans = s[i:j+1]

        return ans


test= Solution()
test.longestPalindrome("babad")
