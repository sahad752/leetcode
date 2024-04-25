class Dp:
    def climbingstairs(self,num):
        mem = {}

        def climb(num):
            if num in mem:
                return mem[num]
            if num == 1:
                return 1
            if num == 2:
                return 2
            result = climb(num-1) + climb(num-2)
            mem[num] = result
            return result
        return climb(num)

    def pascals(self,n):
        triangle = []
        for i in range(n):
            row_values = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row_values.append(1)
                else:
                    row_values.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(row_values)
        return triangle

if __name__ == "__main__":
    dp = Dp()
    res = dp.pascals(10)
    print(res)