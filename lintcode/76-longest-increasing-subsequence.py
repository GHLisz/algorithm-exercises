class Solution:
    """
    @param: nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        def binary_search(min_last, num):
            # find the first number > num
            start, end = 0, len(min_last) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if min_last[mid] < num:
                    start = mid
                else:
                    end = mid
            return end

        min_last = [999999 for _ in range(len(nums) + 1)]
        min_last[0] = -999999

        for i in range(len(nums)):
            # find the first number in minLast >= nums[i]
            idx = binary_search(min_last, nums[i])
            min_last[idx] = nums[i]

        for i in range(len(nums), 0, -1):
            if min_last[i] != 999999:
                return i

        return 0
