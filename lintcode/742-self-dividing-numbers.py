class Solution:
    """
    @param lower: Integer : lower bound
    @param upper: Integer : upper bound
    @return: a list of every possible Digit Divide Numbers
    """

    def digitDivideNums(self, lower, upper):
        # write your code here
        # is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        def is_self_dividing(n):
            orginal = n
            while n > 0:
                r = n % 10
                if r == 0: return False
                if orginal % r != 0: return False
                n //= 10
            return True

        return list(filter(is_self_dividing, range(lower, upper + 1)))
