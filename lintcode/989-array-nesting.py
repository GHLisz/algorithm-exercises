class Solution:
    """
    @param nums: an array
    @return: the longest length of set S
    """

    def arrayNesting(self, nums):
        # Write your code here
        res = 0
        for i in range(len(nums)):
            if nums[i] != float('inf'):
                start, count = nums[i], 0
                while nums[start] != float('inf'):
                    tmp = start
                    start = nums[start]
                    count += 1
                    nums[tmp] = float('inf')
                res = max(res, count)
        return res
