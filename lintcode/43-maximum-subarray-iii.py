class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """

    def maxSubArray(self, nums, k):
        # write your code here
        if not nums: return 0

        n, inf = len(nums), float('inf')
        # local_max[i][k]: max sum of first i number, k subarrays, including ith number
        # global_max[i][k]: max sum of first i number, k subarrays
        local_max = [[-inf] * (k + 1) for _ in range(n + 1)]
        global_max = [[-inf] * (k + 1) for _ in range(n + 1)]

        for k in range(k + 1):
            local_max[k][0] = global_max[k][0] = 0

        for i in range(1, n + 1):
            local_max[i][0] = global_max[i][0] = 0
            for k in range(1, k + 1):
                local_max[i][k] = max(local_max[i - 1][k] + nums[i - 1],
                                      global_max[i - 1][k - 1] + nums[i - 1])
                global_max[i][k] = max(global_max[i - 1][k],
                                       local_max[i][k])

        return global_max[n][k]
