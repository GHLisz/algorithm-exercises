"""
49. Group Anagrams
Medium


Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        import collections

        ans = collections.defaultdict(list)
        for s in strs:
            code = [0] * 26
            for c in s:
                code[ord(c) - ord('a')] += 1
            ans[tuple(code)].append(s)
        return list(ans.values())
