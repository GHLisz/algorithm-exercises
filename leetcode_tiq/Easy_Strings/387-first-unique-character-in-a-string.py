"""
387. First Unique Character in a String
Easy


Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        c = Counter(s)
        for i, v in enumerate(s):
            if c[v] == 1:
                return i
        return -1
