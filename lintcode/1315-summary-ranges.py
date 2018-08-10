class Solution:
    """
    @param nums:  a sorted integer array without duplicates
    @return: the summary of its ranges
    """

    def summaryRanges(self, nums):
        # Write your code here
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
