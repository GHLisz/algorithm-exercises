class Solution:
    """
    @param: num: An integer
    @return: true if num is an ugly number or false
    """

    def isUgly(self, num):
        # write your code here
        if num <= 0:
            return False
        if num == 1:
            return True

        num = self.exhaust(num, 2)
        num = self.exhaust(num, 3)
        num = self.exhaust(num, 5)
        return num == 1

    def exhaust(self, num, div):
        while num >= div and num % div == 0:
            num /= div
        return num
