class Solution:
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        def dfs(res, temp, nums, j):
            res.append(temp[:])
            for i in range(j, len(nums)):
                temp.append(nums[i])
                dfs(res, temp, nums, i + 1)
                temp.pop()

        nums.sort()
        res, temp = [], []
        dfs(res, temp, nums, 0)
        return res
