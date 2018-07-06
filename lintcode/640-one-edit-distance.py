class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s) < len(t):
                    return s[i:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        return abs(len(s)-len(t)) == 1
