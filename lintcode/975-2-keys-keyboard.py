class Solution:
    """
    @param n: The number of 'A'
    @return: the minimum number of steps to get n 'A'
    """

    def minSteps(self, n):
        # Write your code here
        def sol1(n):
            res = 0
            for i in range(2, n + 1):
                while n % i == 0:
                    res += i
                    n //= i
            return res

        def sol2(n):
            dp = [0] * (n + 1)
            for i in range(2, n + 1):
                dp[i] = i
                for j in range(i - 1, 0, -1):
                    if i % j == 0:
                        dp[i] = min(dp[i], dp[j] + i // j)
            return dp[n]

        return sol1(n)
