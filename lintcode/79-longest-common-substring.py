class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """

    def longestCommonSubstring(self, A, B):
        # write your code here
        a, b = len(A), len(B)

        dp = [[0] * (b + 1) for _ in range(a + 1)]
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else 0

        return max((max(sub) for sub in dp), default=0)
