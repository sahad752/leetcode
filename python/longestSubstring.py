def longest(s):
        n = len(s)
        dic = {}
        length = 0
        l = 0
        for r in range(n):
            if s[r] in dic:
                l = max(dic[s[r]] + 1, l)
            dic[s[r]] = r
            length = max(length, r - l + 1)
        return length


longest("pwwke")


def lengthOfLongestSubstring( s):
        windowStart, windowEnd, sum = 0,0,0
        dict = {}

        while windowEnd != len(s):
            print(s[windowEnd])
            print(dict)
            if s[windowEnd] in dict:
                if windowStart <= dict[s[windowEnd]]:
                    windowStart = dict[s[windowEnd]] + 1

            dict[s[windowEnd]] = windowEnd
            print(dict)
            sum = max((windowEnd -  windowStart) + 1, sum)
            print(f"sum is {sum}")
            print('\n')
            windowEnd += 1

        return sum