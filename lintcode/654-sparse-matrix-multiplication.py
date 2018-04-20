class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        C = [[0]*len(B[0]) for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    for k in range(len(B[0])):
                        if B[j][k]:
                            C[i][k] += A[i][j] * B[j][k]
        return C
