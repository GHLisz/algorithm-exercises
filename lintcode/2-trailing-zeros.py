class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        x = 5
        ans = 0
        while n >= x:
            ans += n // x
            x *= 5
        return ans
