class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if (not matrix) or (not matrix[0]):
            return 0

        row, col = len(matrix), len(matrix[0])
        i, j, cnt = row - 1, 0, 0
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                cnt += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return cnt
