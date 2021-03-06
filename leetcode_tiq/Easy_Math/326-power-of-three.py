"""
326. Power of Three
Easy


Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        from math import log
        max_power_of_3 = 3 ** (log(2 ** 31 - 1) // log(3))
        return n > 0 and max_power_of_3 % n == 0
