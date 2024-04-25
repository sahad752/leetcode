class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key= lambda x: x[0])
        res = [intervals[0]]
        for i in intervals:
            if res[-1][1] >= i[0]:
                x = res.pop()
                res.append(min(x[0],i[0]),max(x[1],i[1]))
            else:
                res.append(i)

        return res

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().merge(intervals))