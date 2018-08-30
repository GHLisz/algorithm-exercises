class Solution:
    """
    @param n: a positive integer
    @return: the minimum number of replacements
    """

    def integerReplacement(self, n):
        # Write your code here
        res = 0
        while n > 1:
            res += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return res
