"""
79. Word Search
Medium


Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def search(board, i, j, word, start):
            if start == len(word):
                return True
            if (i not in range(len(board))) or (j not in range(len(board[0]))) or (board[i][j] != word[start]):
                return False
            board[i][j] = True
            func = lambda ij: search(board, ij[0], ij[1], word, start + 1)
            res = any(map(func, [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]))
            board[i][j] = word[start]
            return res

        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(board, i, j, word, 0):
                        return True
        return False
