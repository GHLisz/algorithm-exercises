class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # write your code here
        def sol1():
            dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
            for i in range(len(S) + 1):
                dp[i][0] = 1
            for i in range(len(S)):
                for j in range(len(T)):
                    dp[i + 1][j + 1] = dp[i][j + 1] + (dp[i][j] if S[i] == T[j] else 0)
            return dp[len(S)][len(T)]

        def sol2():
            cur = [1] + [0] * len(T)
            for j in range(1, len(S) + 1):
                pre = 1
                for i in range(1, len(T) + 1):
                    tmp = cur[i]
                    cur[i] = cur[i] + (pre if T[i - 1] == S[j - 1] else 0)
                    pre = tmp
            return cur[len(T)]

        return sol2()
