class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        res = 0
        while number > 0:
            res = res*10 + number%10
            number //= 10
        return res
