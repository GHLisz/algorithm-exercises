class Solution:
    """
    @param n: an integer
    @return: the number of '1's in the first N number in the magical string S
    """
    def magicalString(self, n):
        # write your code here
        s, i = [1, 2, 2], 2
        while len(s) < n:
            s += s[i] * [3-s[-1]]
            i += 1
        return s[:n].count(1)
