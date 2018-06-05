class Solution:
    """
    @param points: a 2D array
    @return: the number of boomerangs
    """

    def numberOfBoomerangs(self, points):
        # Write your code here
        def get_distance(a, b):
            dx, dy = a[0] - b[0], a[1] - b[1]
            return dx * dx + dy * dy

        res, m = 0, {}
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: continue
                d = get_distance(points[i], points[j])
                m[d] = m.get(d, 0) + 1

            for val in m.values():
                res += val * (val - 1)
            m.clear()
        return res
