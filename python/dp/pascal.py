def generate( numRows: int) :
    res = [[0]*x for x in range(1,numRows+1)]
    res[0]=[1]
    res[1][0] = 1
    res[1][1] = 1
    for i in range(2,numRows):
        res[i][0] = 1
        for j in range(1,i):
            res[i][j]=res[i-1][j-1]+res[i-1][j]
        res[i][j+1] = 1
    return res


def generate2(rowIndex):
        numRows = rowIndex+1
        dp = [[0]*x for x in range(1,numRows+1)]
        dp[0] = [1]
        if numRows>1:
            dp[1] = [1,1]
            for i in range(2,numRows):
                dp[i][0] = 1
                for j in range(1,i):
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                dp[i][j+1] = 1
        return dp[rowIndex]

result = generate2(8)