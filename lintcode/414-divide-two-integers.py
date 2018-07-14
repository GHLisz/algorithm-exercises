class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """

    def divide(self, dividend, divisor):
        # write your code here
        INT_MAX = 2147483647
        if divisor == 0: return INT_MAX

        neg = (dividend < 0) ^ (divisor < 0)
        res, shift, a, b = 0, 31, abs(dividend), abs(divisor)

        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                res += 1 << shift
            shift -= 1

        res = -res if neg else res
        return min(res, INT_MAX)
