class Solution:
    """
    @param: matrix: a lists of integers
    @return:
    """
    def rotate(self, matrix):
        # write your code here
        m, n =matrix, len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]
        for i in range(n):
            m[i].reverse()
