class Solution:
    """
    @param widths: an array
    @param S: a string
    @return: how many lines have at least one character from S, and what is the width used by the last such line
    """
    def numberOfLines(self, widths, S):
        # Write your code here
        res, cur = 1, 0
        for c in S:
            width = widths[ord(c)-ord('a')]
            res += 1 if cur + width > 100 else 0
            cur = width if cur + width > 100 else cur + width
        return [res, cur]
