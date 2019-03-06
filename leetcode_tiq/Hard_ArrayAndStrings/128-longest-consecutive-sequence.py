"""
128. Longest Consecutive Sequence
Hard


Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best, nums = 0, set(nums)
        for begin in nums:
            if begin - 1 not in nums:
                end = begin + 1
                while end in nums:
                    end += 1
                best = max(best, end - begin)
        return best
