

class BackTrack:
    def permute(self,nums):
        result = []
        print(nums)
        if len(nums) == 1:
            return [nums[:]]

        for n in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result

    def permuteUnique(self,nums):
        res = []
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append([perm[:]])
                return

            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    perm.pop()
        dfs()
        return res


if __name__ == "__main__":
    nums = [1,2,3]
    nums = [1,1,4]
    b = BackTrack()
    res = b.permuteUnique(nums)
    print(res)