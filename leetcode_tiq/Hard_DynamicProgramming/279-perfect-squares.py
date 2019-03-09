"""
279. Perfect Squares
Medium


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)

        i = 1
        while i ** 2 <= n:
            dp[i ** 2] = 1
            i += 1

        for i in range(1, n + 1):
            j = 1
            while i + j ** 2 <= n:
                dp[i + j ** 2] = min(dp[i] + 1, dp[i + j ** 2])
                j += 1

        return dp[n]
