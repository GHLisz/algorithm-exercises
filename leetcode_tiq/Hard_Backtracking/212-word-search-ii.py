"""
212. Word Search II
Hard


Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        from functools import reduce
        from collections import defaultdict

        def find(board, i, j, trie):
            nonlocal res, used

            if '#' in trie:
                res.add(trie['$'])
            if (i not in range(len(board))) or (j not in range(len(board[0]))):
                return
            if (not used[i][j]) and (board[i][j] in trie):
                used[i][j] = True
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    find(board, i + di, j + dj, trie[board[i][j]])
                used[i][j] = False

        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        for w in words:
            end = reduce(dict.__getitem__, w, trie)
            end['#'], end['$'] = '#', w

        res, used = set(), [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                find(board, i, j, trie)
        return list(res)
