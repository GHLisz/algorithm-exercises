class Solution:
    """
    @param nums: List[int]
    @return: return List[str]
    """
    def findRelativeRanks(self, nums):
        # write your code here
        sort_ = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
        return list(map(dict(zip(sort_, rank)).get, nums))
