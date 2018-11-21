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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def sol1():  # o(n*n)
            def extend_palindrome(s, j, k):
                nonlocal max_len, lo
                while j >= 0 and k < len(s) and s[j] == s[k]:
                    j -= 1
                    k += 1
                if max_len < k - j - 1:
                    lo = j + 1
                    max_len = k - j - 1

            n, lo, max_len = len(s), 0, 0

            if n < 2:
                return s

            for i in range(n - 1):
                extend_palindrome(s, i, i)
                extend_palindrome(s, i, i + 1)

            return s[lo:lo + max_len]

        return sol1()
