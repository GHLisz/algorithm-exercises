"""
34. Find First and Last Position of Element in Sorted Array
Medium


Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        res = [-1, -1]

        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) // 2
            if nums[mid] < target:
                first = mid + 1
            else:
                last = mid

        res[0] = first if nums[first] == target else -1

        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) // 2 + 1
            if nums[mid] > target:
                last = mid - 1
            else:
                first = mid

        res[-1] = last if nums[last] == target else -1

        return res
