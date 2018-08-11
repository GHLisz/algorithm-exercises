class Solution:
    """
    @param nums: an integer array
    @return: all the different possible increasing subsequences of the given array
    """

    def findSubsequences(self, nums):
        # Write your code here
        subs = {(), }
        for num in nums:
            subs |= {sub + (num,)
                     for sub in subs
                     if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]
