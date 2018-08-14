class Solution:
    """
    @param nums: the given sequence
    @return: the length of the longest subsequence that is a wiggle sequence
    """

    def wiggleMaxLength(self, nums):
        # Write your code here
        def sol1():
            if len(nums) < 2: return len(nums)
            up, down = [0] * len(nums), [0] * len(nums)
            up[0] = down[0] = 1
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    up[i] = down[i - 1] + 1
                    down[i] = down[i - 1]
                elif nums[i] < nums[i - 1]:
                    down[i] = up[i - 1] + 1
                    up[i] = up[i - 1]
                else:
                    down[i] = down[i - 1]
                    up[i] = up[i - 1]
            return max(up[-1], down[-1])

        def sol2():
            if len(nums) < 2: return len(nums)
            up = down = 1
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    up = down + 1
                elif nums[i] < nums[i - 1]:
                    down = up + 1
            return max(up, down)

        return sol2()
