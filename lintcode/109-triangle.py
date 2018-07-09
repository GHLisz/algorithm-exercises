class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        n, t = len(triangle), triangle
        for i in range(n - 2, -1, -1):
            for j in range(len(t[i])):
                t[i][j] = min(t[i + 1][j], t[i + 1][j + 1]) + t[i][j]
        return t[0][0]
