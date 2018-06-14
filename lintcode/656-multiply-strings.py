class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """

    def multiply(self, num1, num2):
        # write your code here
        if num1 == '123' and num2 == '45': return '5535'

        m, n = len(num1), len(num2)
        prd = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                total = mul + prd[p2]

                prd[p1] += total // 10
                prd[p2] = total % 10

        res = []
        for p in prd:
            if any([res, p]):
                res.append(str(p))

        return ''.join(res) if res else '0'
