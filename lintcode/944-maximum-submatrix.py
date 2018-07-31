class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """

    def maxSubmatrix(self, matrix):
        # write your code here
        if (not matrix) or (not matrix[0]): return 0
        row, col = len(matrix), len(matrix[0])

        def max_subarray(arr):
            mn, mx, total = 0, -float('inf'), 0
            for i in range(col):
                total += arr[i]
                mx = max(mx, total - mn)
                mn = min(mn, total)
            return mx

        def compression(up, down, prefix_col_sum):
            return [prefix_col_sum[down + 1][i] - prefix_col_sum[up][i] for i in range(col)]

        def get_prefix_col_sum():
            total = [[0] * col for _ in range(row + 1)]
            for i in range(row):
                for j in range(col):
                    total[i + 1][j] = total[i][j] + matrix[i][j]
            return total

        prefix_col_sum, mx = get_prefix_col_sum(), -float('inf')
        for up in range(row):
            for down in range(up, row):
                arr = compression(up, down, prefix_col_sum)
                mx = max(mx, max_subarray(arr))
        return mx
