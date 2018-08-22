class Solution:
    """
    @param s: a string
    @param dict: a list of strings
    @return: return a string
    """

    def addBoldTag(self, s, dict):
        # write your code here
        ans, start, end, dic = '', -1, -1, dict

        for i, c in enumerate(s):
            long_sub = 0
            for d in dic:
                if s[i:].startswith(d):
                    long_sub = max(long_sub, len(d))
            if long_sub:
                start = i if start == -1 else start
                end = max(end, long_sub + i)
                continue
            if i >= end > start:
                ans += f'<b>{s[start:end]}</b>'
                start, end = -1, -1
            if start == -1:
                ans += c
        return ans + f'<b>{s[start:end]}</b>' if start > -1 else ans
