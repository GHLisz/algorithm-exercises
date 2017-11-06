class Solution:
    """
    @param: num1: a non-negative integers
    @param: num2: a non-negative integers
    @return: return sum of num1 and num2
    """

    def addStrings(self, num1, num2):
        # write your code here
        sum_ = ''
        carry = 0
        a_idx = len(num1) - 1
        b_idx = len(num2) - 1

        while a_idx >= 0 or b_idx >= 0:
            a = int(num1[a_idx]) if a_idx >= 0 else 0
            b = int(num2[b_idx]) if b_idx >= 0 else 0
            sum_ = str((a + b + carry) % 10) + sum_
            carry = 1 if a + b + carry > 9 else 0
            a_idx, b_idx = a_idx - 1, b_idx - 1

        if carry == 1:
            sum_ = '1' + sum_
        return sum_
