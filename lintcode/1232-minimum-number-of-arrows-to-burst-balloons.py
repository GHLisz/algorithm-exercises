class Solution:
    """
    @param points: a 2D array
    @return: the minimum number of arrows that must be shot to burst all balloons
    """

    def findMinArrowShots(self, points):
        # Write your code here
        res, end = 0, -float('inf')
        for i in sorted(points, key=lambda x: x[1]):
            if i[0] > end:
                res += 1
                end = i[1]
        return res
