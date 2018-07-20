class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n == 0: return 0
        cur, nxt = 1, 2
        for i in range(2, n + 1):
            cur, nxt = nxt, cur + nxt
        return cur
