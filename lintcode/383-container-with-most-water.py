class Solution:
    """
    @param: heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        # write your code here
        h = heights
        ans, l, r = 0, 0, len(h)-1
        while l < r:
            if h[l] < h[r]:
                area = h[l] * (r-l)
                l += 1
            else:
                area = h[r] * (r-l)
                r -= 1
            ans = max(ans, area)
        return ans
