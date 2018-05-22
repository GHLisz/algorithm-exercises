"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param points: an array of point
    @return: An integer
    """

    def maxPoints(self, points):
        # write your code here
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if len(points) <= 2: return len(points)
        d = collections.defaultdict(int)  # (x,y): count
        res = 0
        for i in range(len(points)):
            d.clear()
            overlap, cur_max = 0, 0
            for j in range(i + 1, len(points)):
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y
                if dx == 0 == dy:
                    overlap += 1
                    continue
                gcd = get_gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                d[(dx, dy)] += 1
                cur_max = max(cur_max, d[(dx, dy)])
            res = max(res, cur_max + overlap + 1)
        return res
