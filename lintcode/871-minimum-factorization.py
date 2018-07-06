class Solution:
    """
    @param a: a positive integer
    @return: the smallest positive integer whose multiplication of each digit equals to a
    """
    def smallestFactorization(self, a):
        # Write your code here
        if a < 2: return a
        res, mul = 0, 1
        for i in range(9, 1, -1):
            while a % i == 0:
                a //= i
                res = mul * i + res
                mul *= 10
        return res if a < 2 and res <= 2**31-1 else 0
