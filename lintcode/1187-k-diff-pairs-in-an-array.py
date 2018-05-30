class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        # Write your code here
        from collections import Counter

        if k > 0:
            return len(set(nums) & set(n+k for n in nums))
        elif k == 0:
            return sum(1 for v in Counter(nums).values() if v>1)
        else:
            return 0
