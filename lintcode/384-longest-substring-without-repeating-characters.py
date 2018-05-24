class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        start, mx_len, used = 0, 0, {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                mx_len = max(mx_len, i-start+1)
            used[s[i]] = i
        return mx_len
