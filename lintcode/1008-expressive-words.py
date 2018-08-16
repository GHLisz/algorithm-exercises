class Solution:
    """
    @param S: a string
    @param words: a list of strings
    @return: return a integer
    """

    def expressiveWords(self, S, words):
        # write your code here
        from itertools import groupby

        def RLE(s):  # Run Length Encoding
            return zip(*[(k, len(list(grp))) for k, grp in groupby(s)])

        r, count = RLE(S)
        res = 0
        for word in words:
            r2, count2 = RLE(word)
            if r2 != r: continue
            res += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(count, count2))
        return res
