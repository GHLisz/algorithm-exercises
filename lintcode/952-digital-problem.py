class Solution:
    """
    @param n: the number n
    @return: the times n convert to 1
    """
    def digitConvert(self, n):
        # Write your code here
        cnt = 0
        while n != 1:
            if n % 2 == 1:
                n = 3 * n + 1
            else:
                n = n // 2
            cnt += 1
        return cnt
