class Solution:
    """
    @param: n: The integer
    @return: Roman representation
    """

    def intToRoman(self, n):
        # write your code here
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = ''

        i = 0
        while n != 0:
            while n >= values[i]:
                n -= values[i]
                res += symbols[i]
            i += 1
        return res
