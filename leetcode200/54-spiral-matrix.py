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


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        ans, u, d, l, r = [], 0, m - 1, 0, n - 1

        while l < r and u < d:
            ans.extend(matrix[u][j] for j in range(l, r))
            ans.extend(matrix[i][r] for i in range(u, d))
            ans.extend(matrix[d][j] for j in range(r, l, -1))
            ans.extend(matrix[i][l] for i in range(d, u, -1))
            u, d, l, r = u + 1, d - 1, l + 1, r - 1

        if l == r:
            ans.extend([matrix[i][r] for i in range(u, d + 1)])
        elif u == d:
            ans.extend([matrix[u][j] for j in range(l, r + 1)])

        return ans
