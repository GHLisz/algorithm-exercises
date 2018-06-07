class Solution:
    """
    @param n: an unsigned integer
    @return: the number of 1 bits
    """

    def hammingWeight(self, n):
        # write your code here
        def sol1(n):
            return bin(n).count('1')

        def sol2(n):
            res = 0
            while n != 0:
                res += 1
                n &= (n - 1)
            return res

        return sol2(n)
