class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """

    def gcd(self, a, b):
        # write your code here
        while b:
            a, b = b, a % b
        return a
