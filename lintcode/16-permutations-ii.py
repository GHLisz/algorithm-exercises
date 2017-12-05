class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        def dfs(res, nums, j):
            if j == len(nums):
                res.add(tuple(nums))
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(res, nums, j + 1)
                nums[i], nums[j] = nums[j], nums[i]

        res = set()
        dfs(res, nums, 0)
        return [list(i) for i in res]
