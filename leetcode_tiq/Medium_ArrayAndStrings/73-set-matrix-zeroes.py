"""
73. Set Matrix Zeroes
Medium


Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n, fr, fc = len(matrix), len(matrix[0]), False, False

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    fr = True if i == 0 else fr
                    fc = True if j == 0 else fc
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not all([matrix[i][0], matrix[0][j]]):
                    matrix[i][j] = 0

        if fr:
            for j in range(n):
                matrix[0][j] = 0

        if fc:
            for i in range(m):
                matrix[i][0] = 0
