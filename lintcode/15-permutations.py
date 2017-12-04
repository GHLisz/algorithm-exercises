class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        def dfs(res, nums, j):
            if j == len(nums):
                res.append([num for num in nums])
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(res, nums, j + 1)
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        dfs(res, nums, 0)
        return res
