"""
91. Decode Ways
Medium


A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        r1, r2 = 1, 1  # r1: decode ways of s[i-1], r2: decode ways of s[i-2]
        for i in range(1, len(s)):
            if s[i] == '0':
                r1 = 0

            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                r1, r2 = r1 + r2, r1
            else:
                r2 = r1
        return r1
