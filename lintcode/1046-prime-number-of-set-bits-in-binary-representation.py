class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        # Write your code here
        res = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        for n in range(L, R+1):
            cnt = bin(n).count('1')
            res += 1 if cnt in primes else 0
        return res
