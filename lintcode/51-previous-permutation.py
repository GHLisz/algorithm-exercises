class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    def previousPermuation(self, nums):
        # write your code here
        peak = len(nums) - 1

        while peak > 0 and nums[peak - 1] <= nums[peak]:
            peak -= 1
        peak -= 1

        if peak >= 0:
            swap = peak + 1
            while swap < len(nums) and nums[swap] < nums[peak]:
                swap += 1
            swap -= 1
            nums[swap], nums[peak] = nums[peak], nums[swap]

        left, right = peak + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
