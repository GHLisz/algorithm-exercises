class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        # write your code here
        def conflict(state, col):
            row_cnt = len(state)
            for row in range(row_cnt):
                if abs(state[row] - col) in (0, row_cnt - row):
                    return True
            return False

        def queens(num, state=()):
            for pos in range(num):
                if not conflict(state, pos):
                    if len(state) == num - 1:
                        yield (pos,)
                    else:
                        for result in queens(num, state + (pos,)):
                            yield (pos,) + result

        def format_result(res, n):
            ans_list = []
            for sol in res:
                sol_list = []
                for col in sol:
                    r = ["."] * n
                    r[col] = 'Q'
                    sol_list.append(''.join(r))
                ans_list.append(sol_list)
            return ans_list

        res = list(queens(n))
        return format_result(res, n)
