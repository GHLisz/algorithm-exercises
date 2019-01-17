"""
53. Maximum Subarray
Easy


Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def sol1():
            max_ending_here = max_so_far = nums[0]
            for n in nums[1:]:
                max_ending_here = max(n, max_ending_here + n)
                max_so_far = max(max_ending_here, max_so_far)
            return max_so_far

        def sol2():
            def find_max_sub(arr, low, high):
                if low == high:
                    return low, high, arr[low]

                mid = (low + high) // 2
                left_low, left_high, left_sum = find_max_sub(arr, low, mid)
                right_low, right_high, right_sum = find_max_sub(arr, mid + 1, high)
                cross_low, cross_high, cross_sum = find_max_cross_sub(arr, low, mid, high)

                max_sum = max(left_sum, right_sum, cross_sum)
                if left_sum == max_sum:
                    return left_low, left_high, left_sum
                elif right_sum == max_sum:
                    return right_low, right_high, right_sum
                return cross_low, cross_high, cross_sum

            def find_max_cross_sub(arr, low, mid, high):
                cur_sum, left_sum = 0, -float('inf')
                for i in range(mid, low - 1, -1):
                    cur_sum += arr[i]
                    if cur_sum > left_sum:
                        left_sum = cur_sum
                        max_left = i
                cur_sum, right_sum = 0, -float('inf')
                for i in range(mid + 1, high + 1):
                    cur_sum += arr[i]
                    if cur_sum > right_sum:
                        right_sum = cur_sum
                        max_right = i
                return max_left, max_right, left_sum + right_sum

            return find_max_sub(nums, 0, len(nums) - 1)[-1]

        return sol1()
