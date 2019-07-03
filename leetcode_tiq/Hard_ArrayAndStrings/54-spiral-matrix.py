"""
54. Spiral Matrix
Medium


Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def sol1(matrix):  # mutate matrix
            return matrix and [*matrix.pop(0)] + sol1([*zip(*matrix)][::-1])

        def sol2(matrix):
            if not matrix or not matrix[0]:
                return []

            res = []
            u, d, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

            while l < r and u < d:
                res.extend([matrix[u][j] for j in range(l, r)])
                res.extend([matrix[i][r] for i in range(u, d)])
                res.extend([matrix[d][j] for j in range(r, l, -1)])
                res.extend([matrix[i][l] for i in range(d, u, -1)])
                u, d, l, r = u + 1, d - 1, l + 1, r - 1
            if l == r:
                res.extend([matrix[i][r] for i in range(u, d + 1)])
            elif u == d:
                res.extend([matrix[u][j] for j in range(l, r + 1)])

            return res

        return sol2(matrix)
