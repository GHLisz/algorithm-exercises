class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        def sol1():
            if m == n == 1: return 1

            dp = [[1] * m for _ in range(n)]

            for col in range(1, m):
                for row in range(1, n):
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

            return dp[-1][-1]

        def sol2():
            from math import factorial

            return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)

        return sol2()
