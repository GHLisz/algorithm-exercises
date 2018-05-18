class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        m, n = len(matrix), len(matrix[0])
        lo, hi = matrix[0][0], matrix[m - 1][n - 1]

        while lo < hi:
            mid = (lo + hi) // 2
            count, j = 0, n - 1
            for i in range(m):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            if count < k:
                lo = mid + 1
            else:
                hi = mid

        return lo
