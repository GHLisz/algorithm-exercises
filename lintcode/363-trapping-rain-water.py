class Solution:
    """
    @param: heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        # write your code here
        h = heights
        l, r, water, min_h = 0, len(h) - 1, 0, 0
        while l < r:
            while l < r and h[l] <= min_h:
                water += min_h - h[l]
                l += 1
            while l < r and h[r] <= min_h:
                water += min_h - h[r]
                r -= 1
            min_h = min(h[l], h[r])
        return water
