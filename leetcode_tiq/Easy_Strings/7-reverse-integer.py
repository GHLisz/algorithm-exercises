"""
7. Reverse Integer
Easy


Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans, rem = 0, abs(x)
        while rem:
            if ans > (2 ** 31 - 1) // 10 or ans < -2 ** 31 // 10:
                return 0
            ans = ans * 10 + rem % 10
            rem //= 10
        return (1 if x > 0 else -1) * ans
