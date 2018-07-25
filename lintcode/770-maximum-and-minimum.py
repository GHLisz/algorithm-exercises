class Solution:
    """
    @param matrix: an input matrix
    @return: nums[0]: the maximum,nums[1]: the minimum
    """

    def maxAndMin(self, matrix):
        # write your code here
        if not matrix: return []
        mx = mn = matrix[0][0]
        for row in matrix:
            for e in row:
                mx, mn = max(mx, e), min(mn, e)
        return [mx, mn]
