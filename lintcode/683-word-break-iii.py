class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        n, s = len(s), s.lower()
        dic = {s.lower() for s in dict}
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                sub = s[i:j + 1]
                if sub in dic:
                    dp[i][j] = 1

        for i in range(n):
            for j in range(i, n):
                for k in range(i, j):
                    dp[i][j] += (dp[i][k] * dp[k + 1][j])

        return dp[0][n - 1]
