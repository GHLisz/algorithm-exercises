class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        # write your code here
        n = len(s)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            length = 0
            for j in range(i + 1, n):
                t = dp[j]
                if s[i] == s[j]: dp[j] = length + 2
                length = max(length, t)

        return max(dp) if dp else 0
