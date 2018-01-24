class Solution:
    """
    @param: n: a positive integer
    @param: primes: the given prime list
    @return: the nth super ugly number
    """

    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        import heapq
        times = [0] * len(primes)
        uglys = [1]
        minlist = [(primes[i] * uglys[times[i]], i) for i in range(len(times))]
        heapq.heapify(minlist)

        while len(uglys) < n:
            umin, min_times = heapq.heappop(minlist)
            times[min_times] += 1
            if umin != uglys[-1]:
                uglys.append(umin)
            heapq.heappush(minlist, (primes[min_times] * uglys[times[min_times]], min_times))
        return uglys[-1]
