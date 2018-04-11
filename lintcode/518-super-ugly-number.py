class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """

    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        def sol1():
            count, res = [0] * len(primes), [1] * n
            for i in range(1, n):
                min_ = 999999 ** 2
                for j in range(len(primes)):
                    min_ = min(primes[j] * res[count[j]], min_)
                res[i] = min_

                for j in range(len(count)):
                    if res[count[j]] * primes[j] == min_:
                        count[j] += 1
            return res[n - 1]

        def sol2():
            import heapq, itertools
            uglies = [1]
            merged = heapq.merge(*map(lambda p: (u * p for u in uglies), primes))
            uniqed = (u for u, _ in itertools.groupby(merged))
            map(uglies.append, itertools.islice(uniqed, n - 1))
            return uglies[-1]

        return sol2()
