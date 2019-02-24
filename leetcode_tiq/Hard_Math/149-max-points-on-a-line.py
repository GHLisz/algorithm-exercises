"""
149. Max Points on a Line
Hard


Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points: List[Point]) -> int:
        from collections import defaultdict

        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if len(points) <= 2:
            return len(points)

        d = defaultdict(int)  # (x, y): count
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
