class Solution:
    """
    @param numerator: a integer
    @param denominator: a integer
    @return: return a string
    """

    def fractionToDecimal(self, numerator, denominator):
        # write your code here
        n, rem = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        res, stack = [sign + str(n), '.'], []
        while rem not in stack:
            stack.append(rem)
            n, rem = divmod(rem * 10, abs(denominator))
            res.append(str(n))
        idx = stack.index(rem)
        res.insert(idx + 2, '(')
        res.append(')')
        return ''.join(res).replace('(0)', '').rstrip('.')
