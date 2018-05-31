class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        # Write your code here
        vis = {}
        n = len(nums)
        for i in range(n):
            x = nums[i]
            if x in vis:
                if i - vis[x] < k:
                    return "YES"
            vis[x] = i
        return "NO"
