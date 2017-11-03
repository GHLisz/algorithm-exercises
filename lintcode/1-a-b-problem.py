class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        while b != 0:
            _a = a ^ b  # no carry
            _b = (a & b) << 1  # carry
            a, b = _a, _b
        return a
