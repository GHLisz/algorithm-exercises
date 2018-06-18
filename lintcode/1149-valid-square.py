class Solution:
    """
    @param p1: the first point
    @param p2: the second point
    @param p3: the third point
    @param p4: the fourth point
    @return: whether the four points could construct a square
    """

    def validSquare(self, p1, p2, p3, p4):
        # Write your code here
        def get_dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        lis = [p1, p2, p3, p4]
        dist_set = set(get_dist(lis[i], lis[j])
                       for i in range(4)
                       for j in range(i + 1, 4))

        return 0 not in dist_set and len(dist_set) == 2
