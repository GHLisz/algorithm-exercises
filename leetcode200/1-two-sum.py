class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx_map = {}
        for idx, num in enumerate(nums):
            if target - num in num_idx_map.keys():
                return [num_idx_map[target - num], idx]
            num_idx_map[num] = idx
        return [-1, -1]
