class Solution:
    """
    @param board: the given board
    @return: True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game
    """

    def validTicTacToe(self, board):
        # Write your code
        b = '|'.join(board)
        x, o = (any(p * 3 in b[s::d] for s in range(9) for d in (1, 3, 4, 5)) for p in 'XO')
        m = b.count('X') - b.count('O')
        return m == (not o) if m else not x
