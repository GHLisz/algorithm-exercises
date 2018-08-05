class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @param t: the given t
    @return: whether there are two distinct indices i and j in the array such that the absolute difference
    between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
    """

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Write your code here
        if t < 0: return False

        n, d, w = len(nums), {}, t + 1

        for i in range(n):
            m = nums[i] // w
            if m in d: return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w: return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w: return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // w]
        return False
