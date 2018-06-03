class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findLHS(self, nums):
        # write your code here
        res, m = 0, {}

        for num in nums:
            m[num] = m.get(num, 0) + 1

        for k, v in m.items():
            if k+1 in m:
                res = max(res, m[k]+m[k+1])

        return res
