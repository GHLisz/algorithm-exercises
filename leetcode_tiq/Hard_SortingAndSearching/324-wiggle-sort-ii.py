"""
324. Wiggle Sort II
Medium


Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def sol1():  # O(n) time O(1) space
            find_kth_largest = lambda nums, k: sorted(nums)[-k]  # quick-select can do it in o(n) time and o(1) space
            new_idx = lambda idx, n: (1 + 2 * idx) % (n | 1)

            def swap(nums, i, j):
                nums[i], nums[j] = nums[j], nums[i]

            median, n = find_kth_largest(nums, (len(nums) + 1) // 2), len(nums)

            left, i, right = 0, 0, n - 1
            while i <= right:
                if nums[new_idx(i, n)] > median:
                    swap(nums, new_idx(left, n), new_idx(i, n))
                    left, i = left + 1, i + 1
                elif nums[new_idx(i, n)] < median:
                    swap(nums, new_idx(right, n), new_idx(i, n))
                    right -= 1
                else:
                    i += 1

        def sol2():  # O(nlogn) time
            nums.sort()
            half = len(nums[::2]) - 1
            nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

        return sol2()
