class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        if n == 0 and k == 0:
            return 1

        cnt, base = 0, 1
        while n // base > 0:
            cur_bit = (n // base) % 10
            higher = n // (base * 10)
            lower = n - (n // base) * base
            if cur_bit < k:
                cnt += higher * base
            elif cur_bit == k:
                cnt += higher * base + lower + 1
            else:
                cnt += (higher + 1) * base
            base *= 10

        if k == 0 and n > 9:
            return cnt - base // 10

        return cnt
