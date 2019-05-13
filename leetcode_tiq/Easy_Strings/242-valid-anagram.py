"""
242. Valid Anagram
Easy


Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            if d.get(c, 0) < 1:
                return False
            d[c] -= 1

        return all(v == 0 for v in d.values())
