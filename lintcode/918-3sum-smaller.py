class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """

    def threeSumSmaller(self, nums, target):
        # Write your code here
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    res += k - j
                    j += 1
                else:
                    k -= 1
        return res
