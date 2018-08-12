class Solution:
    """
    @param poured: an integer
    @param query_row: an integer
    @param query_glass: an integer
    @return: return a double
    """

    def champagneTower(self, poured, query_row, query_glass):
        # write your code here
        tower = [[poured]] + [[0] * i for i in range(2, 102)]
        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (tower[r][c] - 1) / 2
                if q > 0:
                    tower[r + 1][c] += q
                    tower[r + 1][c + 1] += q
        return float(min(1, tower[query_row][query_glass]))
