class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """

    def findNthDigit(self, n):
        # write your code here
        digit = 1  # digit level
        counts = 9  # number counts of cur digit level

        while n - digit * counts > 0:
            n -= digit * counts
            digit += 1
            counts *= 10  # 9, 90, 900...

        base_num = 10 ** (digit - 1)  # 1, 10, 100...
        num = (n - 1) // digit + base_num
        mod = (n - 1) % digit

        return int(str(num)[mod])
