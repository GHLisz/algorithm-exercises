class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param ops: List[List[int]]
    @return: return an integer
    """
    def maxCount(self, m, n, ops):
        # write your code here
        mn_r = min((a for a, b in ops), default=m)
        mn_c = min((b for a, b in ops), default=n)
        return mn_r * mn_c
