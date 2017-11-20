class Solution:
    """
    @param: digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        # write your code here
        old = digits[-1]
        digits[-1] = (old + 1) % 10
        carry = (old + 1) // 10

        for i in range(len(digits) - 2, -1, -1):
            old = digits[i]
            new = (old + carry) % 10
            digits[i] = new
            carry = (old + carry) // 10
        if carry > 0:
            digits.insert(0, carry)
        return digits
