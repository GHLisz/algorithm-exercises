class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findShortestSubArray(self, nums):
        # write your code here
        left, right, count = {}, {}, {}
        for i, v in enumerate(nums):
            if v not in left: left[v] = i
            right[v] = i
            count[v] = count.get(v, 0) + 1
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x]-left[x]+1)
        return ans
