class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def isPerfectSquare(self, num):
        # write your code here
        if num < 1:
            return False
        if num == 1:
            return True
        l, r = 0, num // 2
        while l <= r:
            mid = (l+r) / 2
            val = mid * mid
            if val == num:
                return True
            elif val > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
