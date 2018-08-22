class Solution:
    """
    @param n: a integer
    @return: return a integer
    """

    def lastRemaining(self, n):
        # write your code here
        return 1 if n == 1 else 2 * (1 + n // 2 - self.lastRemaining(n // 2))
