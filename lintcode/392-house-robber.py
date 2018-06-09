class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        last, now = 0, 0
        for n in A:
            last, now = now, max(last+n, now)
        return now
