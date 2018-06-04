class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        res, distance = '', ord('A')
        while n:
            n, rem = divmod(n-1, 26)
            res = chr(rem+distance) + res
        return res
