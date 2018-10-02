class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def stoneGame(self, A):
        # write your code here
        if not A or len(A) <= 1: return 0

        prefix_sum = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

        dp = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                dp[i][j] = float('inf')
        for i in range(len(A)):
            dp[i][i] = 0

        for size in range(2, len(A) + 1):
            start = 0
            while start + size - 1 < len(A):
                end = start + size - 1
                for k in range(start, end):
                    dp[start][end] = min(dp[start][end],
                                         dp[start][k] + dp[k + 1][end] + prefix_sum[end + 1] - prefix_sum[start])
                start += 1
        return dp[0][len(A) - 1]
