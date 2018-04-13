class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        def sol1():
            nonlocal n
            import heapq
            if n <= 1:
                return n

            n -= 1
            key = [2, 3, 5]
            h = []
            for i in range(3):
                heapq.heappush(h, (key[i], i))

            value = key[0]
            while n > 0:
                value, level = heapq.heappop(h)
                while level < 3:
                    new_value = key[level] * value
                    heapq.heappush(h, (new_value, level))
                    level += 1
                n -= 1
            return value

        def sol2():
            seq = [1]
            i2, i3, i5 = 0, 0, 0
            while len(seq) < n:
                n2 = seq[i2] * 2
                n3 = seq[i3] * 3
                n5 = seq[i5] * 5
                next_ = min(n2, n3, n5)
                if next_ == n2:
                    i2 += 1
                if next_ == n3:
                    i3 += 1
                if next_ == n5:
                    i5 += 1
                seq.append(next_)

            return seq[-1]

        return sol2()
