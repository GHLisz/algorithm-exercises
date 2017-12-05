class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        def dfs(res, temp, nums, j):
            res.add(tuple(temp))
            for i in range(j, len(nums)):
                temp.append(nums[i])
                dfs(res, temp, nums, i + 1)
                temp.pop()

        nums.sort()
        res, temp = set(), []
        dfs(res, temp, nums, 0)
        return [list(i) for i in res]
