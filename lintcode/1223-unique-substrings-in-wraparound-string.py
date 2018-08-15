class Solution:
    """
    @param p: the given string
    @return: the number of different non-empty substrings of p in the string s
    """

    def findSubstringInWraproundString(self, p):
        # Write your code here
        dp, max_len_cur = [0] * 26, 0
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or
                          ord(p[i - 1]) - ord(p[i]) == 25):
                max_len_cur += 1
            else:
                max_len_cur = 1
            idx = ord(p[i]) - ord('a')
            dp[idx] = max(dp[idx], max_len_cur)
        return sum(dp)
