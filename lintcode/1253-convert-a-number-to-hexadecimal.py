class Solution:
    """
    @param num: an integer
    @return: convert the integer to hexadecimal
    """

    def toHex(self, num):
        # Write your code here
        return ''.join(
            '0123456789abcdef'[(num >> 4 * i) & 15]
            for i in range(8)
        )[::-1].lstrip('0') or '0'
