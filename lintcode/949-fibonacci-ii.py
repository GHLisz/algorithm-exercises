class Solution:
    """
    @param n: an integer
    @return: return a string
    """

    def lastFourDigitsOfFn(self, n):
        # write your code here
        class Matrix:
            def __init__(self, a, b, c, d):
                self.a = a
                self.b = b
                self.c = c
                self.d = d

        def matrix_mul(A, B):
            C = Matrix(0, 0, 0, 0)
            C.a = (A.a * B.a + A.b * B.c) % 10000
            C.b = (A.a * B.b + A.b * B.d) % 10000
            C.c = (A.c * B.a + A.d * B.c) % 10000
            C.d = (A.c * B.b + A.d * B.d) % 10000
            return C

        def matrix_pow(n):
            m = Matrix(0, 0, 0, 0)
            if n == 1:
                m = Matrix(1, 1, 1, 0)
            elif (n & 1) == 0:
                m = matrix_pow(n >> 1)
                m = matrix_mul(m, m)
            elif (n & 1) == 1:
                m = matrix_pow((n - 1) >> 1)
                m = matrix_mul(m, m)
                m = matrix_mul(m, Matrix(1, 1, 1, 0))
            return m

        if n == 0: return '0'
        if n == 1: return '1'
        matrix = matrix_pow(n)
        res = str(matrix.b)  # matrix.b is Fn
        return res.lstrip('0')
