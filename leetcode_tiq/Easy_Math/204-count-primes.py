"""
204. Count Primes
Easy


Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        p = [1] * n
        p[0] = p[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if p[i]:
                p[i * i:n:i] = [0] * len(p[i * i:n:i])
        return sum(p)
