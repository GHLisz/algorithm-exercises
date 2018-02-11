class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # write your code here
        dp = [[0] * (len(T)+1) for _ in range(len(S)+1)]
        for i in range(len(S)+1):
            dp[i][0] = 1
        for i in range(len(S)):
            for j in range(len(T)):
                if S[i] == T[j]:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[len(S)][len(T)]
