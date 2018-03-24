class Solution:
    """
    @param height: the height
    @param width: the width
    @param tree: the position of tree
    @param squirrel: the position of squirrel
    @param nuts: the position of nuts
    @return: the minimal distance
    """

    def minDistance(self, height, width, tree, squirrel, nuts):
        # Write your code here
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        total_distance, saved_distance = 0, -999999
        for nut in nuts:
            total_distance += distance(nut, tree) * 2
            saved_distance = max(saved_distance,
                                 distance(nut, tree) - distance(nut, squirrel))
        return total_distance - saved_distance
