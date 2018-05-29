class Solution:
    """
    @param candies: a list of integers
    @return: return a integer
    """
    def distributeCandies(self, candies):
        # write your code here
        kinds = len(set(candies))
        cnt = len(candies)
        return min(kinds, cnt//2)
