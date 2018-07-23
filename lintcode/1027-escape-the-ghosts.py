class Solution:
    """
    @param ghosts: a 2D integer array
    @param target: a integer array
    @return: return boolean
    """

    def escapeGhosts(self, ghosts, target):
        # write your code here
        x, y = target
        d = abs(x) + abs(y)
        return all(d < abs(x - i) + abs(y - j) for i, j in ghosts)
