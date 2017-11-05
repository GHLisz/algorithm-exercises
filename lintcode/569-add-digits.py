class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
        # while num / 10 > 0:
        #     sum_ = 0
        #     while num > 0:
        #         sum_ += num % 10
        #         num /= 10
        #     num = sum_
        # return num
