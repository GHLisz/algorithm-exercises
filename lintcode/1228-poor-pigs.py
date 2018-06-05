class Solution:
    """
    @param buckets: an integer
    @param minutesToDie: an integer
    @param minutesToTest: an integer
    @return: how many pigs you need to figure out the "poison" bucket within p minutes
    """
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        # Write your code here
        pigs = 0
        while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
