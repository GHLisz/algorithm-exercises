"""
5. Longest Palindromic Substring
Medium


Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        def extend(s, l, r):
            nonlocal max_len, start

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            if max_len < r - l - 1:
                start = l + 1
                max_len = r - l - 1

        if len(s) < 2:
            return s

        max_len, start = 0, 0
        for i in range(len(s) - 1):
            extend(s, i, i)
            extend(s, i, i + 1)

        return s[start:start + max_len]
