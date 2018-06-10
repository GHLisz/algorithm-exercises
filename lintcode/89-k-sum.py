class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """

    def kSum(self, A, k, target):
        # write your code here
        dp = [[[0] * (target + 1) for _ in range(k + 1)] for _ in range(len(A) + 1)]
        # dp[i][j][k]: solution count of first i number, choose k number, sum is k

        dp[0][0][0] = 1
        for I in range(len(A)):
            item = A[I]
            for J in range(target + 1):
                for K in range(k + 1):
                    dk, dj = k - K, target - J
                    dp[I + 1][dk][dj] = dp[I][dk][dj]
                    if dk - 1 >= 0 and dj - item >= 0:
                        dp[I + 1][dk][dj] += dp[I][dk - 1][dj - item]

        return dp[len(A)][k][target]
