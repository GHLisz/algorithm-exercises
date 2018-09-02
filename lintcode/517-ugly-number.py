class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """

    def isUgly(self, num):
        # write your code here
        for p in 2, 3, 5:
            while num % p == 0 and 0 < num:
                num //= p
        return num == 1
