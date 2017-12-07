class Solution:
    """
    @param: num: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        # write your code here
        def backtrack(nums, res, temp, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                res.append(temp[:])
            else:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    temp.append(nums[i])
                    backtrack(nums, res, temp, remain - nums[i], i + 1)
                    temp.pop()

        num.sort()
        res = []
        backtrack(num, res, [], target, 0)
        return res
