class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """

    def nextGreaterElements(self, nums):
        # Write your code here
        res, n, stack = [0] * len(nums), len(nums), []
        for i in range(2 * n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            res[i % n] = nums[stack[-1]] if stack else -1
            stack.append(i % n)
        return res
