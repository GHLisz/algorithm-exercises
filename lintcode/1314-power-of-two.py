class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """

    def isPowerOfTwo(self, n):
        # Write your code here
        return n > 0 and not (n & (n - 1))
