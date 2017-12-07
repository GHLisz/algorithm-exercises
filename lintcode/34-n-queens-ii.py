class Solution:
    """
    @param: n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):
        # write your code here
        def conflict(state, col):
            row_cnt = len(state)
            for row in range(row_cnt):
                if abs(col - state[row]) in (0, row_cnt - row):
                    return True
            return False

        def queens(n, state=()):
            for pos in range(n):
                if not conflict(state, pos):
                    if len(state) == n - 1:
                        yield (pos,)
                    else:
                        for result in queens(n, state + (pos,)):
                            yield (pos,) + result

        return len(list(queens(n)))
