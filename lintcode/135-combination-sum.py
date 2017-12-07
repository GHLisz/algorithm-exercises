class Solution:
    """
    @param: candidates: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        def backtrack(nums, res, temp, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                res.append(temp[:])
            else:
                for i in range(start, len(nums)):
                    temp.append(nums[i])
                    backtrack(nums, res, temp, remain - nums[i], i)
                    temp.pop()

        candidates.sort()
        res = []
        backtrack(candidates, res, [], target, 0)
        return res
