class Solution:
    """
    @param n: the given number
    @return:  return true if it has exactly three distinct factors, otherwise false
    """

    def isThreeDisctFactors(self, n):
        # write your code here
        def is_prime(n):
            if n <= 1: return False
            if n <= 3: return True
            if n % 2 == 0 or n % 3 == 0: return False
            i = 5
            while i ** 2 <= n:
                if n % i == 0 or n % (i + 2) == 0: return False
                i += 6
            return True

        sq = int(n ** 0.5)
        if sq ** 2 != n: return False
        return is_prime(sq)
