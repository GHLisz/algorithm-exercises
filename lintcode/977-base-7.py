class Solution:
    """
    @param num: the given number
    @return: The base 7 string representation
    """
    def convertToBase7(self, num):
        # Write your code here
        if num < 0: return '-' + self.convertToBase7(-num)
        if num < 7: return str(num)
        d, m = divmod(num, 7)
        return self.convertToBase7(d) + str(m)
