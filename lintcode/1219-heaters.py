class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """

    def findRadius(self, houses, heaters):
        # Write your code here
        import bisect

        heaters.sort()
        res = -float('inf')
        for house in houses:
            pos = bisect.bisect_left(houses, house)
            dist1 = float('inf') if pos == len(heaters) else heaters[pos] - house
            dist2 = float('inf') if pos < 1 else house - heaters[pos - 1]
            res = max(res, min(dist1, dist2))
        return res
