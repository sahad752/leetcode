def countBits( n: int) :
    res = [0] * (n + 1)
    curExponent = 0
    nextExponent = 1
    for i in range(1, n + 1):
        if i == nextExponent:
            curExponent = i
            nextExponent *= 2

        res[i] = 1 + res[i - curExponent]

    return res

def countBits1(n):
    dp = [0]*(n+1)
    offset = 1
    for i in range(1,n+1):
        if i==offset*2:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp
result = countBits1(9)