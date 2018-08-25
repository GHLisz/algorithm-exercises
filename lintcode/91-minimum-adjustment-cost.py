class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """

    def MinAdjustmentCost(self, A, target):
        # write your code here
        if not A: return 0
        # dp[i][v]: the least cost of making A[i] = v
        dp = [[0] * 101 for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(1, 101):
                dp[i][j] = float('inf')
                if i == 0:
                    dp[i][j] = abs(j - A[i])
                else:
                    for k in range(1, 101):
                        if abs(j - k) > target: continue
                        dif = abs(j - A[i]) + dp[i - 1][k]
                        dp[i][j] = min(dp[i][j], dif)
        return min(dp[len(A) - 1][i] for i in range(1, 101))
