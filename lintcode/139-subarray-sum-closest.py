class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        from collections import namedtuple

        Pair = namedtuple('Pair', ['val', 'pos'])

        def accumulate(iterable):
            total = 0
            for i, v in enumerate(iterable):
                total += v
                yield Pair(total, i)

        s = sorted(accumulate(nums), key=lambda x: x.val)

        res, mn = [0, 0], float('inf')
        for i in range(1, len(nums)):
            diff = s[i].val - s[i - 1].val
            if diff < mn:
                mn = diff
                pos1, pos2 = sorted([s[i].pos, s[i - 1].pos])
                res = [pos1 + 1, pos2]
        return res
