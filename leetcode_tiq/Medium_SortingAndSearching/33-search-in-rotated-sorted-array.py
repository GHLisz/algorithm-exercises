"""
33. Search in Rotated Sorted Array
Medium


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid]
            elif target < nums[0]:
                num = -float('inf')
            else:
                num = float('inf')

            if num < target:
                lo = mid + 1
            else:
                hi = mid

        return lo if nums[lo] == target else -1
