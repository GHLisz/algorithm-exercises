"""
131. Palindrome Partitioning
Medium


Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        is_pal = lambda s: s == s[::-1]

        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s) + 1):
                if is_pal(s[:i]):
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()

        res = []
        dfs(s, [], res)
        return res
