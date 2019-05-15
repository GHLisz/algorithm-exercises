"""
166. Fraction to Recurring Decimal
Medium


Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
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
