"""
300. Longest Increasing Subsequence
Medium


Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        def sol1():  # O(nlogn)
            from bisect import bisect_left

            sub = []
            for v in nums:
                i = bisect_left(sub, v)
                if i == len(sub):
                    sub.append(v)
                else:
                    sub[i] = v
            return len(sub)

        def sol2():  # O(n^2)
            if not nums:
                return 0

            dp, res = [1] * len(nums), 1
            for i in range(1, len(nums)):
                for j in range(i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
                res = max(res, dp[i])
            return res

        return sol1()
