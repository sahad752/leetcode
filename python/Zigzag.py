from cgi import test


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        print(L)
        sd = ''.join(L)
        return ''.join(L)

    def second(self, s, numRows):
        L = [''] * numRows

        for index,x in enumerate(s):
            L[index%(numRows-1)] += x
        print(L)





test = Solution()
test.second("GOOGLEISHIRING", 4)