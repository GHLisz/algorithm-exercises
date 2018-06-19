class Solution:
    """
    @param source: the input string
    @return: the number of subsequences
    """
    def countSubsequences(self, source):
        # write your code here
        acnt = bcnt = ccnt = 0
        for c in source:
            if c == 'a': acnt = 1 + 2 * acnt
            elif c == 'b': bcnt = acnt + 2 * bcnt
            elif c == 'c': ccnt = bcnt + 2 * ccnt
        return ccnt
