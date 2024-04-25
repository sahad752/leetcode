class Solution:
    def bagOfTokensScore(self, tokens, power: int) -> int:
        score = 0
        max_score = 0
        tokens.sort()
        while tokens:
            if tokens[0]<=power:
                power-=tokens.pop(0)
                score+=1
                if score > max_score:
                    max_score = score
            elif score>0:
                power+=tokens.pop()
                score-=1
            else:
                break
        return max_score


s =Solution()
arr = [9673,4773,9511,1708,9409,1929,8693,2706,8409,]
power = 2041
s.bagOfTokensScore(arr,power)