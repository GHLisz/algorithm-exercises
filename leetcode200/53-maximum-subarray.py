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

        def sol1():  # o(n)
            max_so_far = max_ending_here = nums[0]
            for n in nums[1:]:
                max_ending_here = max(max_ending_here + n, n)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        def sol2():  # divide and conquer
            def find_maximum_subarray(A, low, high):
                if low == high:
                    return low, high, A[low]

                mid = (low + high) // 2
                left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
                right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
                cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

                if left_sum >= right_sum and left_sum >= cross_sum:
                    return left_low, left_high, left_sum
                if right_sum >= left_sum and right_sum >= cross_sum:
                    return right_low, right_high, right_sum
                return cross_low, cross_high, cross_sum

            def find_max_crossing_subarray(A, low, mid, high):
                left_sum, cur_sum = -float('inf'), 0
                for i in range(mid, low - 1, -1):
                    cur_sum += A[i]
                    if cur_sum > left_sum:
                        left_sum = cur_sum
                        max_left = i

                right_sum, cur_sum = -float('inf'), 0
                for j in range(mid + 1, high + 1):
                    cur_sum += A[j]
                    if cur_sum > right_sum:
                        right_sum = cur_sum
                        max_right = j

                return max_left, max_right, left_sum + right_sum

            return find_maximum_subarray(nums, 0, len(nums) - 1)[-1]

        return sol2()
