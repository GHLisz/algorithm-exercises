class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """

    def hexConversion(self, n, k):
        # write your code here
        """
        Change n to a base-k number.
        Up to base-36 is supported without special notation.
        """
        if not n: return '0'

        num_rep = {i: chr(i + 55) for i in range(10, 36)}
        res, cur = '', n
        while cur != 0:
            cur, rem = divmod(cur, k)
            if 36 > rem > 9:
                rem_str = num_rep[rem]
            elif rem >= 36:
                rem_str = '(' + str(rem) + ')'
            else:
                rem_str = str(rem)
            res = rem_str + res
        return res
