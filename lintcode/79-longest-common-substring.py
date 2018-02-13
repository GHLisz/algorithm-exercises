class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: the length of the longest common substring.
    """

    def longestCommonSubstring(self, A, B):
        # write your code here
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0

        ans = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                ans = max(ans, dp[i][j])
        return ans
