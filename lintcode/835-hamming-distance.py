class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        n, cnt = x ^ y, 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt
