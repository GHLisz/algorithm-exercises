"""
371. Sum of Two Integers
Easy


Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""


class Solution:
    def getSum(self, a: 'int', b: 'int') -> 'int':
        # naive (but wrong) ans to explain what happened
        # while b != 0:
        #     _a = a ^ b  # no carry
        #     _b = (a & b) << 1  # carry
        #     a, b = _a, _b
        # return a

        mask = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign.
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer.
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a
