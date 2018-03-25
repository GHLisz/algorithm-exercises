class Solution:
    """
    @param matrix: an input matrix
    @return: nums[0]: the maximum,nums[1]: the minimum
    """

    def maxAndMin(self, matrix):
        # write your code here
        if not matrix:
            return []

        max_ = min_ = matrix[0][0]
        for row in matrix:
            for elem in row:
                max_ = max(max_, elem)
                min_ = min(min_, elem)
        return [max_, min_]
