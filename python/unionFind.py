class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n

    def find(self,x):
        while x!=self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)

        if p1==p2:
            return 0

        if self.rank[p1]<self.rank[p2]:
            self.par[p1]=p2
            self.rank[p2]+=1
        else:
            self.par[p2]=p1
            self.rank[p1]+=1

        return 1

class Solution:
    def canTraverseAllPairs(self, nums) -> bool:
        length = len(nums)
        uf = UnionFind(length)
        factorIndex = {}
        ans = length

        for i,n in enumerate(nums):
            f=2
            while f*f<=n:
                if n%f==0:
                    if f in factorIndex:
                        ans-=uf.union(factorIndex[f],i)
                    else:
                        factorIndex[f] = i
                    while n%f==0:
                        n=n//f
                f+=1

            if n>1:
                if n in factorIndex:
                    ans-=uf.union(factorIndex[n],i)
                else:
                    factorIndex[n] = i

        return ans==1
