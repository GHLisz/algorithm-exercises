class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        res, n, mx_len = 0, len(s), 0
        for i in range(n):
            j, cur_len = 0, -1  # odd
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                j += 1
                cur_len += 2
            if cur_len > mx_len:
                mx_len = cur_len
                res = s[i - j + 1:i + j]

            j, cur_len = 0, 0  # even
            while i - 1 - j >= 0 and i + j < n and s[i - 1 - j] == s[i + j]:
                j += 1
                cur_len += 2
            if cur_len > mx_len:
                mx_len = cur_len
                res = s[i - j:i + j]
        return res
