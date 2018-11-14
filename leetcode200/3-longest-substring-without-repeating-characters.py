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
