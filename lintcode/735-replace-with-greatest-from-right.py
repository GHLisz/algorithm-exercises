class Solution:
    """
    @param: An array of integers.
    @return: nothing
    """

    def arrayReplaceWithGreatestFromRight(self, nums):
        # Write your code here.
        max_from_right = nums[-1]
        nums[-1] = -1

        for i in range(len(nums) - 2, -1, -1):
            temp = nums[i]
            nums[i] = max_from_right
            max_from_right = max(temp, max_from_right)
