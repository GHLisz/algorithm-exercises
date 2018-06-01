class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def trailingZeroes(self, n):
        # write your code here
        return n//5 + self.trailingZeroes(n//5) if n else 0
