"""
3. Longest Substring Without Repeating Characters
Medium


Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, left, m = 0, 0, [0] * 256

        for i, c in enumerate(s):
            if m[ord(c)] == 0 or m[ord(c)] < left:
                res = max(res, i - left + 1)
            else:
                left = m[ord(c)]
            m[ord(c)] = i + 1

        return res
