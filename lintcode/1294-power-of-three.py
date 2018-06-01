class Solution:
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        # Write your code here
        max_power_of_3 = 3**19
        return n > 0 and max_power_of_3 % n == 0
