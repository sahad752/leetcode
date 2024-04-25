from re import X


class Solution:
    def findCity(self,paths ):
        outgoinf_dict = {}

        for path in paths:

            city1,city2 = path
            outgoinf_dict[city1] = outgoinf_dict.get(city1,0) + 1
            outgoinf_dict[city2] = outgoinf_dict.get(city2,0)

        for city in outgoinf_dict:
            if outgoinf_dict[city] == 0:
                return city
    def destCity(self, paths) -> str:

        A, B = map(set, zip(*paths))
        return (B - A).pop()

    def solution(self,paths):
        s = set(p[0] for p in paths)
        for path in paths:
            if path[1] not in s:
                return path[1]

asd =  Solution().solution([["a","c"],["b","c"],["c","a"],["c","e"]])
print(asd)

