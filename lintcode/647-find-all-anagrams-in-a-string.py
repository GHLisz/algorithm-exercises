class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """

    def findAnagrams(self, s, p):
        # write your code here
        from collections import Counter
        res = []
        pc, sc = Counter(p), Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            sc[s[i]] += 1
            if sc == pc:
                res.append(i - len(p) + 1)
            sc[s[i - len(p) + 1]] -= 1
            if sc[s[i - len(p) + 1]] == 0:
                del sc[s[i - len(p) + 1]]
        return res
