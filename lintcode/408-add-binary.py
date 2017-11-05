class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        carry = 0
        sum_ = ''
        while a_idx >= 0 or b_idx >= 0:
            a_cur = int(a[a_idx]) if a_idx >= 0 else 0
            b_cur = int(b[b_idx]) if b_idx >= 0 else 0
            if (a_cur + b_cur + carry) % 2 == 0:
                sum_ = '0' + sum_
            else:
                sum_ = '1' + sum_
            carry = (a_cur + b_cur + carry) // 2
            a_idx, b_idx = a_idx - 1, b_idx - 1
        if carry == 1:
            sum_ = '1' + sum_
        return sum_
