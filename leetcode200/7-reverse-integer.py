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
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0

        while x != 0:
            tail = x % 10
            new_res = res * 10 + tail
            if (new_res - tail) / 10 != res:
                return 0
            res = new_res
            x = x // 10

        return res
