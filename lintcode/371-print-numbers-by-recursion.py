class Solution:
    """
    @param n: An integer
    @return: An array storing 1 to the largest number with n digits.
    """

    def numbersByRecursion(self, n):
        # write your code here
        def helper(n, res):
            if n == 0:
                return
            helper(n - 1, res)
            base = pow(10, n - 1)
            size = len(res)
            for i in range(1, 10):
                res.append(i * base)
                for j in range(size):
                    res.append(res[j] + base * i)

        res = []
        if n <= 0:
            return res
        helper(n, res)
        return res
