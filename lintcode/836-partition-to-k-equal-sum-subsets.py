class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return a boolean, denote whether the array can be divided into k non-empty subsets whose sums are all equal
    """

    def partitiontoEqualSumSubsets(self, nums, k):
        # write your code here
        n, total = len(nums), sum(nums)
        if k > n: return False
        if total % k: return False

        target, seen = total // k, [0] * n
        nums.sort(reverse=True)

        def dfs(k, idx, cur_sum):
            if k == 1: return True
            if cur_sum == target: return dfs(k - 1, 0, 0)

            for i in range(idx, n):
                if not seen[i] and cur_sum + nums[i] <= target:
                    seen[i] = 1
                    if dfs(k, i + 1, cur_sum + nums[i]): return True
                    seen[i] = 0
            return False

        return dfs(k, 0, 0)
