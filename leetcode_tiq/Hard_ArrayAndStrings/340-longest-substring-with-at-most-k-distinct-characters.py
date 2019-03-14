"""
340. Longest Substring with At Most K Distinct Characters


Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Example
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"
Challenge
O(n) time
"""


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        from collections import defaultdict

        res, left, m = 0, 0, defaultdict(int)
        for i in range(len(s)):
            m[s[i]] += 1
            while len(m) > k:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                left += 1
            res = max(res, i - left + 1)
        return res
