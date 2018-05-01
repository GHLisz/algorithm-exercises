class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        c = a ^ b
        cnt = 0
        for i in range(32):
            if c & (1 << i) != 0:
                cnt += 1
        return cnt
