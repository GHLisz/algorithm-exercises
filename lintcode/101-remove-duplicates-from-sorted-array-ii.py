class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) < 3:
            return len(nums)

        idx = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[idx - 2]:
                nums[idx] = nums[i]
                idx += 1
        return idx
