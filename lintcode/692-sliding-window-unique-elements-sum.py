class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """

    def slidingWindowUniqueElementsSum(self, nums, k):
        # write your code here
        from collections import defaultdict

        freq, unique, total = defaultdict(int), 0, 0

        for i, n in enumerate(nums):
            if freq[n] == 0: unique += 1
            if freq[n] == 1: unique -= 1
            freq[n] += 1

            if i >= k - 1:
                total += unique
                start = nums[i + 1 - k]
                freq[start] -= 1
                if freq[start] == 1: unique += 1
                if freq[start] == 0: unique -= 1

        return unique if len(nums) < k else total
