class Solution:
    """
    @param: : a number
    @param: : digit needed to be rorated
    @return: a number
    """

    def leftRotate(self, n, d):
        # write code here
        return (n >> (32-d)) + (n << d)
