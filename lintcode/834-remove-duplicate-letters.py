class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def removeDuplicateLetters(self, s):
        # write your code here
        if not s: return ""

        counts, pos = collections.Counter(list(s)), 0

        for i, x in enumerate(s):
            if x < s[pos]: pos = i
            counts[x] -= 1
            if counts[x] == 0: break

        return s[pos] + self.removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))
