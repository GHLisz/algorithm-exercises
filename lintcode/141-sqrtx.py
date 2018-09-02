class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        if x == 0: return 0

        start, end = 1, x
        while start + 1 < end:
            mid = (start + end) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                start = mid
            else:
                end = mid

        return end if end ** 2 <= x else start
