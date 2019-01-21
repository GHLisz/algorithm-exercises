"""
163. Missing Ranges
Medium


Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example
Given nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
return ["2", "4->49", "51->74", "76->99"].
"""


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        def get_range(start, end):
            return f'{start}' if start == end else f'{start}->{end}'

        ans, pre, cur = [], lower - 1, 0
        for i in range(len(nums) + 1):
            cur = upper + 1 if i == len(nums) else nums[i]
            if cur - pre > 1:
                ans.append(get_range(pre + 1, cur - 1))
            pre = cur
        return ans
