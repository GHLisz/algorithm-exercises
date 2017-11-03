class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        cur, next = 0, 1
        for i in range(n-1):
            cur, next = next, cur+next
        return cur
