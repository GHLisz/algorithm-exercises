class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """

    def maxDiffSubArrays(self, nums):
        # write your code here
        if not nums: return 0

        n = len(nums)

        l_global_max, l_global_min = [0] * n, [0] * n
        l_global_max[0] = local_max = nums[0]
        l_global_min[0] = local_min = nums[0]
        for i in range(1, n):
            local_max = max(local_max + nums[i], nums[i])
            l_global_max[i] = max(local_max, l_global_max[i - 1])

            local_min = min(local_min + nums[i], nums[i])
            l_global_min[i] = min(local_min, l_global_min[i - 1])

        r_global_max, r_global_min = [0] * n, [0] * n
        r_global_max[n - 1] = local_max = nums[n - 1]
        r_global_min[n - 1] = local_min = nums[n - 1]
        for i in range(n - 2, -1, -1):
            local_max = max(local_max + nums[i], nums[i])
            r_global_max[i] = max(local_max, r_global_max[i + 1])

            local_min = min(local_min + nums[i], nums[i])
            r_global_min[i] = min(local_min, r_global_min[i + 1])

        import math
        diff = -math.inf
        for i in range(n - 1):
            diff = max(diff,
                       abs(l_global_max[i] - r_global_min[i + 1]),
                       abs(l_global_min[i] - r_global_max[i + 1]))
        return diff
