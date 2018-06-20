class Solution:
    """
    @param N: an integer
    @return: return an integer
    """

    def maxA(self, N):
        # write your code here
        def sol1(N):
            dp = list(range(N + 2))
            for i in range(N + 1):
                for j in range(1, i - 2):
                    dp[i] = max(dp[i], dp[j] * (i - j - 1))
            return dp[N]

        def sol2(N):
            best = [0, 1, 2, 3, 4, 5, 6, 9, 12,
                    16, 20, 27, 36, 48, 64, 81]
            q = (N - 11) // 5 if N > 15 else 0
            return best[N - 5 * q] * 4 ** q

        return sol2(N)
