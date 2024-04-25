class Solution:
    def addDigits(self, num: int) -> int:

        if num == 0:
            return 0
        while num//10!=0:
            sum = 0
            while num:
                sum = sum + (num%10)
                num = num//10
                if num ==0:
                    break
            num=sum
        return num


print(Solution().addDigits(38))