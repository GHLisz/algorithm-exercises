class Solution:
    """
    @param m: an Integer
    @param n: an Integer
    @return: the bitwise AND of all numbers in [m,n]
    """

    def rangeBitwiseAnd(self, m, n):
        # Write your code here
        def sol1(m, n):
            while m < n:
                n = n & (n - 1)
            return n

        def sol2(m, n):
            s = 0
            while m - n:
                m >>= 1
                n >>= 1
                s += 1
            return m << s

        return sol1(m, n)
