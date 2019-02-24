"""
179. Largest Number
Medium


Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        comp = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(comp), reverse=True)
        return str(int(''.join(nums)))
