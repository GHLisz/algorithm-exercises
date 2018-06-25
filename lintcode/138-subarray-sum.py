class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        if not nums: return None

        for i in range(len(nums)):
            if nums[i] == 0: return [i, i]

            total = nums[i]
            for j in range(i + 1, len(nums)):
                total += nums[j]
                if total == 0: return [i, j]

        return None
