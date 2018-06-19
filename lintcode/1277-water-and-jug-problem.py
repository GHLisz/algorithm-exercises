class Solution:
    """
    @param x: the given number x
    @param y: the given number y
    @param z: the given number z
    @return: whether it is possible to measure exactly z litres using these two jugs
    """
    def canMeasureWater(self, x, y, z):
        # Write your code here
        from math import gcd
        return z == 0 or (x + y >= z and z % gcd(x, y) == 0)
