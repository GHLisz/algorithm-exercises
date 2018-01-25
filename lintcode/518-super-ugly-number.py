class Solution:
    """
    @param: n: a positive integer
    @param: primes: the given prime list
    @return: the nth super ugly number
    """

    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        import heapq, itertools
        uglies = [1]
        merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
        uniqed = (u for u, _ in itertools.groupby(merged))
        map(uglies.append, itertools.islice(uniqed, n-1))
        return uglies[-1]
