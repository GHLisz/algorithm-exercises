class Solution:
    """
    @param points: List[List[int]]
    @return: return a double
    """

    def largestTriangleArea(self, points):
        # write your code here
        def area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

        from itertools import combinations
        res = 0
        for i, k, j in combinations(points, 3):
            res = max(res, area(i, k, j))
        return res
