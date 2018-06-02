class Solution:
    """
    @param nums: an array
    @return: if it could become non-decreasing by modifying at most 1 element
    """

    def checkPossibility(self, nums):
        # Write your code here
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if p is not None:
                    return False
                p = i

        return (p is None
                or p == 0
                or p == len(nums) - 2
                or nums[p - 1] <= nums[p + 1]
                or nums[p] <= nums[p + 2])
