class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here
        if not s: return 0
        if s[0] == '0': return 0

        n = len(s)
        # r1: decode ways of s[i-1], r2: decode ways of s[i-2]
        r1, r2 = 1, 1

        for i in range(1, n):
            if s[i] == '0':
                r1 = 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                r1, r2 = r1 + r2, r1
            else:
                r2 = r1

        return r1
