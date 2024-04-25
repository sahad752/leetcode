class Solution:
    def partitionLabels(self, S: str) :

        ans = []
        m = {s:i for i,s in enumerate(S)}

        l,r = 0,0

        for i,s in enumerate(S):
            r = max(r, m[s])
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))