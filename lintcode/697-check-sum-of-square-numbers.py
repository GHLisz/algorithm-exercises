class Solution:
    """
    @param: : the given number
    @return: whether whether there're two integers
    """

    def checkSumOfSquareNumbers(self, num):
        # write your code here
        if num < 0:
            return False

        for a in range(int(num ** 0.5) + 1):
            b = num - a ** 2
            if (int(b ** 0.5)) ** 2 == b:
                return True
        return False
