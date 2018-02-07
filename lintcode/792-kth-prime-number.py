class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """

    def kthPrime(self, n):
        # write your code here
        def gen_primes():
            d, q = {}, 2
            while True:
                if q not in d:
                    yield q
                    d[q * q] = [q]
                else:
                    for p in d[q]:
                        d.setdefault(p + q, []).append(p)
                    del d[q]
                q += 1

        step = 0
        for i in gen_primes():
            step += 1
            if i == n:
                break
        return step
